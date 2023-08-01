from flask import Flask,render_template,request
import chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    return str(chatbot.get_response(user_input))

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
