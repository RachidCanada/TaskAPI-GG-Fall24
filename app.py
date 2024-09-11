from flask import Flask, jsonify
from views.task_view import task
from views.user_view import user
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.url_map.strict_slashes = False

app.register_blueprint(task)
app.register_blueprint(user)

@app.errorhandler(404)
def errorHandler(self):
    return jsonify({"error": "404, Something went wrong!"}), 404

@app.route("/")
def index():
    return "<h1>Home</h1>"

if __name__ == "__main__":
    app.run()