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
    'SII': 101,
    'NII': 102,
    'HII': 103,
    'X': 104,
    'XII': 5,
    'Ft': 6,
    'S预备生': 150,
    '荣誉毕业生': 199,
    '未入列': 149,
    # u'预备生': 7,
    # u'未列队': 7,
    'SNH48': 151,
    'B': 201,
    'E': 202,
    'J': 203,
    '预备生': 210,
    'BEJ48': 211,
    'G': 301,
    'NIII': 302,
    'Z': 303,
    '未列队': 304,
    'G预备生': 305,

    '新成员': 304,
    'SIII': 401,
    'HIII': 402,
    'C': 501,
    'K': 502,
    'CKG48': 505,
    'idft': 701
}
