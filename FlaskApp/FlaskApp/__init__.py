from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin? We're gonna build the NBA site 2.0'


if __name__ == "__main__":
    app.run()
