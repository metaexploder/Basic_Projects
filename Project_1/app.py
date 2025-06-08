from flask import Flask, render_template, request, Response

app = Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username") #request jo form m aayi h usse get kr lo username jo aaya h 
    password = request.form.get("password")

    users = {
        "vishal" : "123",
        "admin" : "456",
        "gaurav" : "789"
    }

    if username in users and password == users[username]:
        return render_template("welcome.html", name = username)
    else:
        return Response("In-valid credintials. Try agian", mimetype = "text/plain")



