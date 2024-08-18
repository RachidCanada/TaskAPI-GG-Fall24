from flask import Flask, jsonify
from views.task_view import task
from views.user_view import user

app = Flask(__name__)

app.register_blueprint(task)
app.register_blueprint(user)

@app.errorhandler(404)
def errorHandler(self):
    return jsonify({"error": "404, Something went wrong!"}), 404

@app.route("/")
def index():
    return "Home"

if __name__ == "__main__":
    app.run()