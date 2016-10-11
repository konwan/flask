# flask

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
