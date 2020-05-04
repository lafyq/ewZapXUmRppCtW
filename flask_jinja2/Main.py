import threading
import uuid

import VmessGetter
from queue import Queue


q = Queue(maxsize=1)

""" 入队 """
def q_put():
    global q
    q.put(VmessGetter.py_main())  # 入队

""" 出队 """
def q_get():
    global q
    return q.get()  # 出队


"""
获取订阅链接内容
"""
def tx_get():
    print("main.tx....")
    global q
    if(q.empty()):
        q_put()
    vmess_str = q_get()
    t1 = threading.Thread(target=q_put)     # 开一条线程put
    t1.start()
    return vmess_str




"""
1. 写入订阅链接内容
2. 返回订阅链接全路径
"""
def get_vmess_url():
    vmess_str = tx_get()

    vmess_url = "static/" + str(uuid.uuid4())
    with open(vmess_url, 'wb') as f:
        f.write(vmess_str)

    vmess_url = "http://127.0.0.1:5000/" + vmess_url

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



