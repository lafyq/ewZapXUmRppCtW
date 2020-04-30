import requests
from bs4 import BeautifulSoup


def send_email(email_address):
    url = 'https://freemycloud.xyz/auth/send'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Referer': 'https://freemycloud.xyz/auth/register',
    }

    formdata = {'email': email_address}

    s = requests.Session()
    r = s.post(url, data=formdata, headers=headers)

    if(r.status_code == 200):
        return 1
    else:
        return 0


def reg(email_address, emailcode):
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

    s = requests.Session()
    r = s.post(url, data=formdata, headers=headers)

    if(r.status_code == 200):
        return 1
    else:
        return 0


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

    s = requests.Session()
    r = s.post(url, data=formdata, headers=headers)

    r.status_code = 0
    while(r.status_code != 200):
        r = s.get("https://freemycloud.xyz/user")       # 确保进入用户中心

    return r




def get_vmess_str(email_address):
    r = login(email_address)

    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)

    str_raw = None
    str_raw = soup.findAll(name="button", attrs={"class": "btn btn-pill btn-v2ray mb-3 copy-text"})
    # print(str_raw)
    while(str_raw == None):
        get_vmess_str(email_address)

    str_target = None
    str_target = "".join('%s' % id for id in str_raw)
    while(str_target == None):
        get_vmess_str(email_address)
    # print(str_target)

    index_start = str_target.index('http')
    index_end = str_target.index('sub=3')
    vmess_str = str_target[index_start:index_end + 5]
    while(vmess_str == ""):
        get_vmess_str(email_address)        # 说明没有加载到vemss，我们太快了，再来几次

    print(vmess_str)  # 订阅地址，最终需转发
    return vmess_str
