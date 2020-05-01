from bs4 import BeautifulSoup
import requests
import base64

# 获取到vmess机场地址
def get_vmess_url(content):

    soup = BeautifulSoup(content, 'html.parser')

    str_raw = soup.findAll(name="button", attrs={"class": "btn btn-pill btn-v2ray mb-3 copy-text"})

    str_target = "".join('%s' % i for i in str_raw)

    index_start = str_target.index('http')
    index_end = str_target.index('sub=3')
    vmess_url = str_target[index_start:index_end + 5]


    print(vmess_url)  # 订阅地址，最终需转发
    return vmess_url



# 改为我们的机场地址
def change(vmess_url):
    response = requests.get(vmess_url)

    raw = str(response.content, encoding="utf-8")
    print(raw)

    temp = str(base64.b64decode(raw), encoding="utf-8")  # 解码

    # 想了好久只能用这种方法了
    idx = 0
    for i in range(2):
        idx = temp.index("vmess", idx + 5)
    t = temp[idx:]

    my_vmess_url = base64.b64encode(t.encode('utf-8'))  # 编码
    print(str(my_vmess_url, 'utf-8'))

    return my_vmess_url

# change("https://freemycloud.site/link/SUMSAcXgGGaEgXdu?sub=3")