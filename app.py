from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('member.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)