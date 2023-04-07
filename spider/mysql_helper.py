# !/usr/bin/python
# coding:utf-8

import logging
import pymysql

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
    'passwd': 'root',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'snh48',
    'charset': 'utf8',
    'use_unicode': True
}


class MySQLHelper:
    def __init__(self):
        try:
            self.connection = pymysql.connect(**prod_config)
        except Exception as e:
            logging.exception(e)

    def execute(self, sql):
        """
        针对insert, delete, update操作
        :param sql:
        :return:
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            logging.exception(e)
            self.connection.rollback()

    def select(self, sql):
        """
        读操作
        :param sql:
        :return:
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            logging.exception(e)

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


mysql_helper = MySQLHelper()
