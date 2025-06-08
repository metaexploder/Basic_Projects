from flask import Flask, render_template, request, Response

app = Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username") #request jo form m aayi h usse get kr lo username jo aaya h 
    password = request.form.get("password")

    if username == "admin" and password == "admin":
        return render_template("welcome.html", name = username)
    else:
        return Response("In-valid credintials. Try agian", mimetype = "text/plain")



