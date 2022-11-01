from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello This is my new website for Laptop repair, you can call us over 9999999999</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
