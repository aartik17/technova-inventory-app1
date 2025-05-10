from flask import Blueprint, request, redirect, url_for

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == "admin":
        return redirect(url_for('home'))
    return {"status": "success", "user": username}