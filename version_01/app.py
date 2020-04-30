from flask import Flask
import Main

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Main.py_main()


if __name__ == '__main__':
    app.run()
