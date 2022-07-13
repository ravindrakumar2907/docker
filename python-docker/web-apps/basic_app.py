import os
from turtle import color
import tkinter as TK
from flask import Flask, render_template

app = Flask(__name__)

color = os.environ.get("APP_COLOR")
if not color:
    color = "red"
    
@app.route("/h")
def demo():
    return "server is runing fine"

@app.route("/index")
def index_view():
    return render_template('index.html', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)