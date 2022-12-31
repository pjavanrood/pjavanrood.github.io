from flask import Flask,  render_template, request, session, flash, redirect, url_for, jsonify
import smtplib
import os


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/kamino')
def kamino():
    return render_template("projectsHTML/kamino.html")

@app.route('/twitter')
def twitter():
    return render_template("projectsHTML/twitter.html")


@app.route('/market')
def market():
    return render_template("projectsHTML/market.html")


@app.route('/algo')
def algo():
    return render_template("projectsHTML/algo.html")


@app.route('/brick')
def brick():
    return render_template("projectsHTML/brick.html")


@app.route('/claw')
def claw():
    return render_template("projectsHTML/claw.html")


@app.route('/frenzy')
def frenzy():
    return render_template("projectsHTML/frenzy.html")


@app.route('/gas')
def gas():
    return render_template("projectsHTML/gas.html")


@app.route('/form', methods=['POST'])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    format_message = name + "\n" + subject + "\n" + email + "\n" + message



    sender = os.environ.get('sitemail')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, os.environ.get('mailpass'))
    

    try:
    
        server.sendmail(from_addr=sender, to_addrs=sender, msg=format_message)
        return jsonify(message="OK")
    except:
        return jsonify(message="fail")

