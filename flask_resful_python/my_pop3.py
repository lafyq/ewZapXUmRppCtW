from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import web_reg_and_login
import time

import poplib


# indent用于缩进显示:
def print_info(msg, indent=0):
    html = ""
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            # print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            # print('%spart %s' % ('  ' * indent, n))
            # print('%s--------------------' % ('  ' * indent))
            # print_info(part, indent + 1)
            None
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            # print('%sText: %s' % ('  ' * indent, content + '...'))
            html = html + content
        else:
            # print('%sAttachment: %s' % ('  ' * indent, content_type))
            None

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


def get_emailcode(html):
    # idx = html.index('602652')    # index验证码的出来的索引位置
    emailcode = html[6769:6775]  # 获取到验证码
    print(emailcode)
    return emailcode


def login_email(email_address, email_password):
    M = poplib.POP3('pop.163.com')
    M.user(email_address)
    M.pass_(email_password)
    numMessages = len(M.list()[1])

    return numMessages, M

def pop3(email_address, email_password):

    server = None
    index = 0
    count = 100
    while(index == 0):
        index, server = login_email(email_address, email_password)
        print("正在努力获取邮件......")
        if(count <= 0):     # 60秒后重新发送邮件
            print("请容我休息60s....................")
            time.sleep(60)
            while (True):
                flag = web_reg_and_login.send_email(email_address)  # 申请发送邮箱验证码
                if (flag == 1):
                    break  # 已经确定按了发送按钮
            count = 100

    resp, lines, octets = server.retr(index)        # 这里要特别注意：有可能是新邮箱，就会索引出0（非法）
                                                    # 索引出0就非法了，因为最小索引是从1开始的
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)

    emailcode = ""
    html = print_info(msg)
    if(html == ""):
        print("html is none")
    else:
        emailcode = get_emailcode(html)
        print("emailcode %s" % emailcode)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()

    return emailcode