from flask import Flask, render_template
import logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
@app.route("/health")
def health():
    return {
        "status": "OK",
        "service": "secure-app",
        "version": "1.0"
    }
@app.route("/")
def home():
    return render_template("index.html")
if __name__== "__main__":
  app.run(host="0.0.0.0", port=5000)
