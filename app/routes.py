from flask import Flask

app = Flask(__name__)

@app.get("/")
def about_me():
    me = {
        "first_name": "Will",
        "last_name": "Quinnan",
        "hobbies": "Video games",
        "active": True
    }

    return me