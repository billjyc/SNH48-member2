# !/usr/bin/python
# coding:utf-8
import MySQLdb
import logging

test_config = {
    'user': 'root',
    'passwd': 'root',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'snh48',
    'charset': 'utf8',
    'use_unicode': True
}

prod_config = {
    'user': 'root',
    'passwd': 'Jyc@1993',
    'host': '112.74.183.47',
    'port': 3306,
    'db': 'snh48',
    'use_unicode': True,
    'charset': 'utf8',
}


class MySQLHelper:
    def __init__(self):
        try:
            self.connection = MySQLdb.connect(**prod_config)
        except Exception as e:
            logging.exception(e)

    def execute(self, sql):
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
