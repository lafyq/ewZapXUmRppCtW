import time

import requests
import poplib

from email.parser import Parser
from email.header import decode_header



# 解析msg
def parse_msg(msg):
    html = ""

    if (msg.is_multipart()):
        parts = msg.get_payload()
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            html = html + content

    return html

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset




# 发送邮件
def send_email(email_address):
    url = 'https://freemycloud.xyz/auth/send'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Referer': 'https://freemycloud.xyz/auth/register',
    }

    formdata = {'email': email_address}

    s = requests.Session()
    r = s.post(url, data=formdata, headers=headers)

    return r.status_code        # 返回状态码让Main去判断


# 登录邮箱并获取邮件索引和邮件服务器对象
def login_and_get_email(email_address, email_password):
    M = poplib.POP3('pop.163.com')
    M.user(email_address)
    M.pass_(email_password)
    numMessages = len(M.list()[1])

    return numMessages, M   # 返回最新一封邮件索引和邮件服务器的对象


# 循环机器人
def robot_login_and_get_email(email_address, email_password):
    index, server = login_and_get_email(email_address, email_password)
    count = 100
    while(index == 0):
        print("正在努力获取邮件......")
        count -= 1
        index, server = login_and_get_email(email_address, email_password)
        if(count < 0):
            print("请容我休息60s....................")
            time.sleep(60)
            count = 100

    return index, server       # 返回最新一封邮件索引和邮件服务器的对象


# 获取emailcode
def get_emailcode(email_address, email_password):
    index, server = robot_login_and_get_email(email_address, email_password)

    resp, lines, octets = server.retr(index)

    msg_content = b'\r\n'.join(lines).decode('utf-8')

    msg = Parser().parsestr(msg_content)

    html = parse_msg(msg)       # 解析成html

    emailcode = html[6769:6775]  # 获取到验证码

    server.quit()

    return emailcode        # 理应返回6为数字的验证码


