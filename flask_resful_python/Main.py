import my_pop3
import web_reg_and_login
import DBUtil
import time
import change_vmess
import offer_html
import datetime

def get_vemss():
    data = DBUtil.get_data()  # 查数据库，获取没用过的邮箱
    email_address = data[1]
    email_password = data[2]

    # web_reg_and_login.send_email(email_address)  # 申请发送邮箱验证码
    # time.sleep(30)  # 必须要休眠，给足对方时间给我们发验证码
    while(True):
        flag = web_reg_and_login.send_email(email_address)  # 申请发送邮箱验证码
        if(flag == 1):
            break           # 已经确定按了发送按钮

    print("邮箱发送成功......")
    while(True):
        emailcode = my_pop3.pop3(email_address, email_password)  # 不停地获取邮箱验证码
        if(emailcode.isdigit()):    # 全是数字时说明就是验证码了
            break

    print("验证码获取成功.....")

    # web_reg_and_login.reg(email_address, emailcode)  # 注册账号
    # time.sleep(10)  # 也要给对方服务器时间响应

    count = 0
    while(count < 60):     # 循环120次
        flag = web_reg_and_login.reg(email_address, emailcode)  # 注册账号
        if(flag == 1):
            break       # 注册成功
        count += 1
        time.sleep(0.5)   # 睡眠0.5秒，节省服务器资源

    if(count >= 60):     # 说明获取status_code不等于200了，注册失败，可能是邮箱的问题
        print("邮箱有问题.......")
        # todo  // 这里要处理这个问题

    print("邮箱注册成功.....")

    vemss = web_reg_and_login.get_vmess_str(email_address)  # 终于可以拿到机场了

    return vemss


def py_main():
    vmess = get_vemss()
    print("机场已经拿到手，准备做转发")
    print(vmess)


    my_vmess = change_vmess.change(vmess)
    # print("我的机场" + str(my_vmess))
    # path = offer_html.save_my_vmess(my_vmess)

    return my_vmess


def count_time():
    start_time = datetime.datetime.now()
    print("尝试运行py_main(): " + str(start_time))

    a = py_main()
    print(a)

    end_time = datetime.datetime.now()
    print("py_main()运行结束: " + str(end_time))

    print("总用时：" + str(end_time - start_time))
    return a