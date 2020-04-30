import requests


# 网站注册
def register(email_address, emailcode):
    url = 'https://freemycloud.xyz/auth/register'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Referer': 'https://freemycloud.xyz/auth/register',
    }

    formdata = {
        'email': email_address,
        'name': 'freemycloud',
        'passwd': 'freemycloud',
        'repasswd': 'freemycloud',
        'code': '',
        'emailcode': emailcode}

    requests.adapters.DEFAULT_RETRIES = 2  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    r = s.post(url, data=formdata, headers=headers)

    return r.status_code


# 网站登录
def login(email_address):
    url = 'https://freemycloud.xyz/auth/login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Referer': 'https://freemycloud.xyz/auth/login',
    }

    formdata = {
        'email': email_address,
        'passwd': 'freemycloud',
        'code': '',
        'remember_me': 'on'}

    requests.adapters.DEFAULT_RETRIES = 2  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    r = s.post(url, data=formdata, headers=headers)

    return r.status_code, s


# 登录机器人
def robot_login(email_address):
    status_code, s = login(email_address)
    print(status_code)
    while (status_code != 200):
        status_code, s = login(email_address)

    return s


# 进入用户中心，返回content
def login_to_user(email_address):
    s = robot_login(email_address)
    resp = s.get("https://freemycloud.xyz/user")
    while (resp.status_code != 200):
        resp = s.get("https://freemycloud.xyz/user")  # 确保进入用户中心

    content = None
    content = resp.text
    return content          # 返回服务器响应的文本

