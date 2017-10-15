
import urllib2
import json
import sys

from spider.mysql_helper import MySQLHelper

reload(sys)
sys.setdefaultencoding('utf8')

# proxy = 'proxy.tencent.com:8080'
# opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy}))
# urllib2.install_opener(opener)


urls = [
    'http://h5.snh48.com/resource/jsonp/members.php?gid=10',  # 上海
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=20',  # 北京
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=30',  # 广州
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=40'  # 沈阳
]

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
    'speciality': 'speciality'
}


mapping_status = {
    '99': 1,  # 在团
    '44': 0   # 暂休
}

mapping_team = {
    'SII': 1,
    'NII': 2,
    'HII': 3,
    'X': 4,
    'XII': 5,
    'B': 201,
    'E': 202,
    'J': 203,
    'G': 301,
    'NIII': 302,
    'Z': 303,
    'SIII': 401,
    'HIII': 402
}


def process_group(group_json, helper):
    rows = group_json['rows']
    for row in rows:
        process_single_member(row, helper)


def process_single_member(row, helper):
    id = int(unicode_to_chinese(row['sid']))
    name = unicode_to_chinese(row['sname'])
    nick_name = unicode_to_chinese(row['nickname'])
    height = int(unicode_to_chinese(row['height']))
    blood_type = unicode_to_chinese(row['blood_type'])
    team = mapping_team[unicode_to_chinese(row['tname'])]
    batch = unicode_to_chinese(row['pname'])
    english_name = unicode_to_chinese(row['pinyin'])
    join_time = unicode_to_chinese(row['join_day'])
    link = 'http://www.snh48.com/member_details.html?sid=%d' % id
    image_link = 'http://www.snh48.com/images/member/zp_%d.jpg' % id
    hobby = unicode_to_chinese(row['hobby'])
    description = unicode_to_chinese(row['experience']).replace('<br>', '\r\n')
    is_valid = mapping_status[unicode_to_chinese(row['status'])]
    constellation = unicode_to_chinese(row['star_sign_12'])
    birth_place = unicode_to_chinese(row['birth_place'])
    agency = unicode_to_chinese(row['company'])
    speciality = unicode_to_chinese(row['speciality'])
    # print id, name, description

    sql = """ update memberinfo
            SET `name`=\'%s\', `nick_name`=\'%s\', `height`=\'%s\', `blood_type`=\'%s\',
            `team`=%d, `batch`=\'%s\', 
            `english_name`=\'%s\', `join_time`=\'%s\', `link`=\'%s\', 
            `image_link`=\'%s\', `hobby`=\'%s\', `description`=\'%s\', 
            `constellation`=\'%s\',`birth_place`=\'%s\', `agency`=\'%s\', 
            `speciality`=\'%s\', `is_valid`=%d WHERE `id`=%d """ % \
          (name, nick_name, height, blood_type, team, batch, english_name, join_time,
        link, image_link, hobby, description, constellation, birth_place, agency, speciality,
           is_valid, id)

    print sql
    helper.execute(sql)
    print 'update'
    # print row


def unicode_to_chinese(uni):
    return str(uni).encode('utf-8')


helper = MySQLHelper()
for url in urls:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    s = response.read()
    # 转换成json
    s_json = json.loads(s, encoding='utf-8')
    response.close()

    print s_json
    process_group(s_json, helper)

# helper.commit()
helper.close_connection()
