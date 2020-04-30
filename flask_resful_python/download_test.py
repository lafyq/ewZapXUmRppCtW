from flask import send_file, send_from_directory
from flask import Flask

app = Flask(__name__)

# @app.route("/download", methods=['GET'])
# def download():
#     # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
#     return send_from_directory("E:\\Workspaces\\PycharmProjects\\flask_resful_python", "v2ray-linux-64.zip", as_attachment=True)

@app.route("/go", methods=['GET'])
def download():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory("E:\\Workspaces\\PycharmProjects\\flask_resful_python", "go.sh", as_attachment=True)



if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/download
