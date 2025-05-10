from flask import Flask
from login import login_bp
app = Flask(__name__)
app.register_blueprint(login_bp)

@app.route('/')
def home():
    return "Welcome to TechNova Inventory Management System!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)