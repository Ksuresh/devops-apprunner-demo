from flask import Flask
import os

app = Flask(__name__)

# ✅ We will change this later to show auto-deploy
MESSAGE = "Hello from AWS App Runner - Version 1"

@app.route("/")
def home():
    return f"""
    <html>
      <body style="font-family: Arial; padding: 40px;">
        <h1>DevOps CI/CD Demo</h1>
        <p><b>Message:</b> {MESSAGE}</p>
        <p><i>Commit change → AWS updates automatically</i></p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
