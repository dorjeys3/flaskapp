from flask import Flask, render_template
  
app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about_me():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

