from flask import Flask, render_template
import Main

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    vmess_url = Main.get_vmess_url()
    vpn = {'vmess': vmess_url}
    return render_template('index.html', title='vpn', vpn=vpn)

if __name__ == '__main__':
        app.run()
