from flask import Flask
import test
import Main

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    # return test.pr()
    return Main.py_main()

if __name__ == '__main__':
    app.run()
