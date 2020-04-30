import requests
import base64

def change(url):
    response = requests.get(url)

    # raw = response.content
    raw = str(response.content, encoding="utf-8")
    print(raw)

    temp = str(base64.b64decode(raw), encoding="utf-8")  # 解码

    # 想了好久只能用这种方法了
    idx = 0
    for i in range(2):
        idx = temp.index("vmess", idx + 5)
    t = temp[idx:]

    temp2 = base64.b64encode(t.encode('utf-8'))  # 编码
    print(str(temp2, 'utf-8'))

    return temp2

# change("https://freemycloud.site/link/SUMSAcXgGGaEgXdu?sub=3")