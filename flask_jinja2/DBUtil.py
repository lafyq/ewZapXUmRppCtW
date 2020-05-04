import datetime
from random import random

import pymysql


def get_email_data():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='163', charset='utf8')
    cursor = db.cursor()
    """
    used = 0 表示没有使用过
    limit 1 表示每次只取一个
    sql = "SELECT id, address, password FROM email where used = 0 limit 1"
    """
    # id = random.randint(1,999)

    sql = "SELECT id, address, password FROM email where used = 0 limit 1"
    cursor.execute(sql)
    data = cursor.fetchone()

    """datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')"""
    id = data[0]
    sql = "update email set used = 1 where id = %d" % id     # 标志为已用过
    cursor.execute(sql)
    db.commit()

    return data
