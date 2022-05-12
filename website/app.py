from flask import Flask, url_for, redirect, render_template

app = Flask("Personnal App")

@app.route("/")
def redirect():
    return redirect(url_for("home"))

@app.route("/gaecko")
def gaecko():
    return render_template("gaecko.html")

if __name__ == "__main__":
    app.run(debug=True)