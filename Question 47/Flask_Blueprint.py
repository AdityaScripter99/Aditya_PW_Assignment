# main.py
from flask import Flask
from user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return "Main Page"

if __name__ == '__main__':
    app.run(debug=True)

# user.py
from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile')
def profile():
    return "User Profile"
