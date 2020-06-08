# !/usr/bin/python
# coding:utf-8


urls = [
    'https://h5.48.cn/resource/jsonp/members.php?gid=10',  # 上海
    # 'https://h5.48.cn/resource/jsonp/members.php?gid=20',  # 北京
    # 'https://h5.48.cn/resource/jsonp/members.php?gid=30',  # 广州
    # 'https://h5.48.cn/resource/jsonp/members.php?gid=40'  # 沈阳
    # 'https://h5.48.cn/resource/jsonp/members.php?gid=50'  # 重庆
    # 'https://h5.48.cn/resource/jsonp/members.php?gid=70'  # IDFT
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
    'Ft': 6,
    # u'预备生': 7,
    # u'未列队': 7,
    'SNH48': 151,
    'B': 201,
    'E': 202,
    'J': 203,
    '预备生': 210,
    'G': 301,
    'NIII': 302,
    'Z': 303,
    '未列队': 304,

    '新成员': 304,
    'SIII': 401,
    'HIII': 402,
    'C': 501,
    'K': 502,
    'idft': 701
}
