# !/usr/bin/python
# coding:utf-8


import requests

from spider.global_config import mapping_team, mapping_status, urls
from spider.mysql_helper import mysql_helper


mapping_column = {
    'sid': 'id',
    'sname': 'name',
    'nickname': 'nickname',
    'pinyin': 'english_name',
    'height': 'height',
    'blood_type': 'blood_type',
    'tname': 'team',
    'pname': 'batch',
    'join_day': 'join_time',
    'hobby': 'hobby',
    'experience': 'description',
    'status': 'is_valid',
    'star_sign_12': 'constellation',
    'birth_place': 'birth_place',
    'company': 'agency',
    'speciality': 'speciality',
    'pid': 'pid'
}


def process_group(group_json):
    rows = group_json['rows']
    for row in rows:
        process_single_member(row)


def process_single_member(row):
    id = int(unicode_to_chinese(row['sid']))
    name = unicode_to_chinese(row['sname'])
    nick_name = unicode_to_chinese(row['nickname'])
    height = int(unicode_to_chinese(row['height']))
    blood_type = unicode_to_chinese(row['blood_type'])
    team = mapping_team[unicode_to_chinese(row['tname'])]
    batch = unicode_to_chinese(row['pname'])
    english_name = unicode_to_chinese(row['pinyin'])
    join_time = unicode_to_chinese(row['join_day'])
    if id > 70000:
        link = 'https://idft.snh48.com/member-detail.html?sid=%d' % id
        image_link = 'https://idft.snh48.com/image/member/zp_%d.jpg' % id
    elif 50000 < id < 60000:
        link = 'http://www.ckg48.com/member_details.html?sid=%d' % id
        image_link = 'http://www.ckg48.com/images/members/zp_%d.jpg' % id
    else:
        link = 'http://www.snh48.com/member_details.html?sid=%d' % id
        image_link = 'http://www.snh48.com/images/member/zp_%d.jpg' % id
    hobby = unicode_to_chinese(row['hobby'])
    description = unicode_to_chinese(row['experience']).replace('<br>', '\r\n')
    is_valid = mapping_status[unicode_to_chinese(row['status'])]
    constellation = unicode_to_chinese(row['star_sign_12'])
    birth_place = unicode_to_chinese(row['birth_place'])
    agency = unicode_to_chinese(row['company'])
    speciality = unicode_to_chinese(row['speciality'])
    pid = int(row['pid'])
    # print id, name, description

    # sql = """ update memberinfo
    #         SET `name`=\'%s\', `nick_name`=\'%s\', `height`=\'%s\', `blood_type`=\'%s\',
    #         `team`=%d, `batch`=\'%s\',
    #         `english_name`=\'%s\', `join_time`=\'%s\', `link`=\'%s\',
    #         `image_link`=\'%s\', `hobby`=\'%s\', `description`=\'%s\',
    #         `constellation`=\'%s\',`birth_place`=\'%s\', `agency`=\'%s\',
    #         `speciality`=\'%s\', `is_valid`=%d, `pid`=%d WHERE `id`=%d """ % \
    #       (name, nick_name, height, blood_type, team, batch, english_name, join_time,
    #     link, image_link, hobby, description, constellation, birth_place, agency, speciality,
    #        is_valid, pid, id)

    sql = """ INSERT INTO memberinfo (`id`, `name`, `nick_name`, `height`, `blood_type`, `team`, `batch`, `english_name`,
    `join_time`, `link`, `image_link`, `hobby`, `description`, `constellation`, `birth_place`, `agency`, 
    `speciality`, `is_valid`, `pid`) VALUES 
    (%d, \'%s\', \'%s\', \'%s\', \'%s\', %d, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\',\'%s\', \'%s\', \'%s\',
    \'%s\', %d, %d) ON DUPLICATE KEY UPDATE `name`=\'%s\', `nick_name`=\'%s\', `height`=\'%s\', `blood_type`=\'%s\',
            `team`=%d, `batch`=\'%s\', 
            `english_name`=\'%s\', `join_time`=\'%s\', `link`=\'%s\', 
            `image_link`=\'%s\', `hobby`=\'%s\', `description`=\'%s\', 
            `constellation`=\'%s\',`birth_place`=\'%s\', `agency`=\'%s\', 
            `speciality`=\'%s\', `is_valid`=%d, `pid`=%d""" % \
          (id, name, nick_name, height, blood_type, team, batch, english_name, join_time,
           link, image_link, hobby, description, constellation, birth_place, agency, speciality,
           is_valid, pid,
           name, nick_name, height, blood_type, team, batch, english_name, join_time,
           link, image_link, hobby, description, constellation, birth_place, agency, speciality,
           is_valid, pid
           )

    print(sql)
    mysql_helper.execute(sql)
    print('update')


def unicode_to_chinese(uni):
    return uni


if __name__ == '__main__':
    for url in urls:
        s_json = requests.get(url, verify=False).json()
        print(s_json)
        process_group(s_json)

    mysql_helper.close_connection()
