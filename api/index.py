from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #if request.method == 'GET':
    return render_template("index.html")
    #return render_template("index.html")

@app.route('/about')
def about():
    return 'About'