import socket
from flask import Flask, request, session, redirect, url_for, jsonify, render_template
import config

app = Flask(__name__)
app.secret_key = "alskdkfhggqpwoeirutyzmxncbcvalalal"


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except OSError:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("ok"):
        return redirect(url_for("scan"))
    error = None
    if request.method == "POST":
        if request.form.get("password") == config.scan_pass:
            session["ok"] = True
            return redirect(url_for("scan"))
        error = "Wrong password"
    return render_template("login.html", error=error)


@app.route("/scan")
def scan():
    if not session.get("ok"):
        return redirect(url_for("login"))
    return render_template("scan.html")


@app.route("/send", methods=["POST"])
def send():
    if not session.get("ok"):
        return jsonify(error="unauthorized"), 401
    code = request.get_json().get("code", "")
    print("Barcode:", code, flush=True)   # terminal me simple print
    return jsonify(status="ok")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    print("For PC:    https://localhost:5000/login")
    print("Mobile:    https://" + get_ip() + ":5000/login")
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
