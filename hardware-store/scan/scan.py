from flask import Flask, request, session, redirect, render_template
import config

app = Flask(__name__)
app.secret_key = "kuch-bhi"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == config.scan_pass:
            session["ok"] = True
            return redirect("/scan")
        return render_template("login.html", msg="Galat password")
    return render_template("login.html", msg="")

@app.route("/scan")
def scan():
    if not session.get("ok"):
        return redirect("/login")
    return render_template("scan.html")

@app.route("/send", methods=["POST"])
def send():
    if not session.get("ok"):
        return "login karo", 401

    print(">>> SCANNED:", request.json["code"], flush=True)
    return "ok"
def get_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == "__main__":
    print("For Pc:    https://localhost:5000/login")
    print("Mobile: https://" + get_ip() + ":5000/login")
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")


