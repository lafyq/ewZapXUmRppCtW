import poplib
import pymysql


count = 1000
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='163', charset='utf8')

def check_pop(data):
    flag = False
    try:
        M = poplib.POP3("pop.163.com")
        M.user(data[1])
        M.pass_(data[2])
        flag = True
    except Exception as e:
        flag = False
    finally:
        return flag


# 获取游标
def get_cursor():
    global db
    cursor = db.cursor()
    sql = "SELECT id, username, password FROM email"
    cursor.execute(sql)
    return cursor

# 获取数据
def get_data(cursor):
    return cursor.fetchone()        # 每调用一次从游标中获取一条数据

# 删除数据
def delete_data(cursor, tuple_delete_id):
    print(tuple_delete_id)
    rowcount = 0
    global db       # 获取全局参数db
    sql = "delete from email where id in %s" % (tuple_delete_id, )    # SQL 删除语句
    try:
        cursor.execute(sql)     # 执行SQL语句
        rowcount = cursor.rowcount
        db.commit()     # 提交修改
        print("delete OK")
    except:
        db.rollback()   # 发生错误时回滚

    return rowcount



def check():
    cursor = get_cursor()       # 获取游标
    list_delete_id = []     # 需要删除的id列表
    delete_count = 0       # 需要删除的行
    global count        # 获取全局变量count
    while (count > 0):
        count = count - 1
        data = get_data(cursor)
        if(data == None):
            break
        else:
            id = data[0]
            print(id)
            flag = check_pop(data)
            if (flag == False):
                list_delete_id.append(id)      # 即将删除的id
                global delete_count
                delete_count += 1
    rowcount = delete_data(cursor, tuple(list_delete_id))       # 需要转成元组
    print("本需删除： %d  条记录！" % delete_count)
    print("实际删除： %d  条记录！" % rowcount)



check()