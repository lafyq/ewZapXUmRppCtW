import threading

import UrlGetter
from queue import Queue


q = Queue(maxsize=1)

def q_put():
    global q
    q.put(UrlGetter.py_main())  # 入队

def q_get():
    global q
    return q.get()  # 出队


# tx获取
def tx_get():
    print("main.tx....")
    global q
    if(q.empty()):
        q_put()
    vmess_url = q_get()
    t1 = threading.Thread(target=q_put)     # 开一条线程put
    t1.start()
    return vmess_url

# 自己到期
def time_out():
    q_get()
    q_put()



# 计时器无法使用
def fun_timer():
    time_out()
    print('Hello Timer!')
    global timer
    timer = threading.Timer(10800, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)

def start_timer():
    print("计时器启动啦。。。。")
    global timer
    timer.start()



