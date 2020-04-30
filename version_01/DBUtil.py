import pymysql

def get_email_data():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Aa112211@', db='163', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT id, username, password FROM email WHERE used01 = 0 limit 1"   # 每次只取一个
    cursor.execute(sql)
    data = cursor.fetchone()

    id = data[0]
    sql = " update email set used01 = 1 where id = %d" % id     # 标志为已用过
    cursor.execute(sql)
    db.commit()

    return data
