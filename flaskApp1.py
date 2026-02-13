from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/aboutUs")
def aboutUs():
    return "<h2>Welcome to CIS 3590</h2>"

@app.route("/contactUs/<string:name>")
def contactUs(name):
    return f"Hi, {name}, call us at 305-348-7852"

if __name__ =='__main__':
    app.run(debug=True)


