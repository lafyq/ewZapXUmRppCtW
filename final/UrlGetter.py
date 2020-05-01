import DBUtil
import EmailTools
import WebTools
import Spider



# py程序的main函数
def py_main():
    data = DBUtil.get_email_data()
    email_address = data[1]
    email_password = data[2]

    print(data)

    robot_send_email(email_address)     # 发送邮件

    print("已发送邮件")

    emailcode = robot_get_emailcode(email_address, email_password)      # 获取邮箱验证码

    print("邮箱验证码：" + emailcode)

    WebTools.register(email_address, emailcode)     # 网站注册

    print("注册成功")

    content = WebTools.login_to_user(email_address)      # 登录并进入用户中心

    print("登陆成功")

    my_vmess_url = Spider.change(Spider.get_vmess_url(content))       # 获取机场地址并改为我们的机场地址

    print("机场已就绪，随时可以转发！！！")

    return my_vmess_url


# 发送邮件
def robot_send_email(email_address):
    status_code = EmailTools.send_email(email_address)
    while(status_code != 200):
        status_code = EmailTools.send_email(email_address)

# 获取邮箱验证码
def robot_get_emailcode(email_address, email_password):
    emailcode = EmailTools.get_emailcode(email_address, email_password)
    while(not emailcode.isdigit()):
        emailcode = EmailTools.get_emailcode(email_address, email_password)

    return emailcode


# 网站注册
def robot_register(email_address, emailcode):
    status_code = WebTools.register(email_address, emailcode)
    while (status_code != 200):
        status_code = WebTools.register(email_address, emailcode)


# 登录并进入用户中心，返回服务器响应的文本
def robot_login_to_user(email_address):
    content = WebTools.login_to_user(email_address)  # 登录并进入用户中心
    while (content == None):
        content = WebTools.login_to_user(email_address)  # 登录并进入用户中心

    return content


