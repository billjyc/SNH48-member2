# !/usr/bin/python
# coding:utf-8


urls = [
    'http://h5.snh48.com/resource/jsonp/members.php?gid=10',  # 上海
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=20',  # 北京
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=30',  # 广州
    # 'http://h5.snh48.com/resource/jsonp/members.php?gid=40'  # 沈阳
]

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