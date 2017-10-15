# coding=utf-8

from weibo import APIClient
import webbrowser
import requests
import logging
import datetime

from mysql_helper import mysql_helper
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


APP_KEY = '3278595304'  # app key
APP_SECRET = 'ec7364d69dd5e6a51498f9583fbf0074'  # app secret
CALLBACK_URL = 'http://112.74.183.47:8081/girls/auth'  # callback url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)


def init():
    url = client.get_authorize_url()
    print url
    # TODO: redirect to url
    # webbrowser.open(url)
    # r = requests.get(url, allow_redirects=False)
    # if 300 <= r.status_code < 400:
    #     print r.headers['location']
    # else:
    #     print 'no redirect'


def get_access_token(code):
    r = client.request_access_token(code)
    access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in  # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # TODO: 在此可保存access token
    client.set_access_token(access_token, expires_in)


def update_member_weibo_info():
    logging.info('update member weibo info')
    # 先获取成员及其对应的uid
    sql = """
        select id, weibo_id from weibo
    """
    records = mysql_helper.select(sql)
    id_weibouid_map = {}
    weibouid_id_map = {}
    for r in records:
        id_weibouid_map[r[0]] = r[1]
        weibouid_id_map[r[1]] = r[0]

    weibo_uids = id_weibouid_map.values()
    length = len(weibo_uids)

    cur = 0
    while cur < length:
        print cur
        size = min(length, cur + 100)
        uids = ''
        for i in range(cur, size):
            uids = '%s,%s' % (uids, weibo_uids[i])
        uids = uids[1:]  # 去掉开头的逗号
        counts = client.users.counts.get(uids=uids)

        for c in counts:
            uid = c['id']
            followers_count = c['followers_count']
            friends_count = c['friends_count']
            statuses_count = c['statuses_count']

            sql1 = """
                UPDATE weibo SET `followers_count`=%d, `friends_count`=%d, `statuses_count`=%d WHERE `weibo_id`=%d
            """ % (followers_count, friends_count, statuses_count, uid)
            mysql_helper.execute(sql1)

            update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sql2 = """
                INSERT INTO weibo_data_history (`id`, `weibo_id`, `followers_count`, `friends_count`, `statuses_count`,
                    `update_time`)
                    VALUES (%d, %d, %d, %d, %d, \'%s\')
            """ % (weibouid_id_map[uid], uid, followers_count, friends_count, statuses_count, update_time)
            mysql_helper.execute(sql2)
        cur += size


if __name__ == '__main__':
    init()
    print 'code='
    code = raw_input()
    get_access_token(code)
    scheduler = BlockingScheduler()
    scheduler.add_job(update_member_weibo_info, 'cron', hour='4')

    try:
        logging.debug('start')
        scheduler.start()
    except Exception as e:
        print e
        print 'shutdown'
        scheduler.shutdown()
