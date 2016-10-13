# flask

https://theblackcat102.wordpress.com/2016/06/30/%E7%94%A8flask%E5%BB%BA%E7%AB%8Brestful-api/
http://seanlin.logdown.com/posts/247948-introduction-to-flask-blueprints

Flask is a microframework for Python based on Werkzeug, 
Jinja 2 and good intentions. It's BSD licensed!

Flask is Fun
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

And Easy to Setup
```
$ pip install Flask
$ python hello.py
 * Running on http://localhost:5000/
```
