from flask import Flask

application = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Article CMS!"

@app.route('/getAToken')
def get_a_token():
    # Placeholder for OAuth callback logic
    return "OAuth token endpoint reached!"

@app.route('/login')
def login():
    # Placeholder for login page or OAuth start
    return "Login page route."

if __name__ == '__main__':
    app.run()
