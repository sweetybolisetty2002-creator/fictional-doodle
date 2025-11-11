from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Article CMS!"

@app.route('/getAToken')
def get_a_token():
    # Placeholder for OAuth callback logic
    return "OAuth token endpoint reached!"

@app.route('/login')
def login():
    # Replace with your actual Azure AD values:
    CLIENT_ID = "9277e643-3ae3-4421-b668-7aa47a48acc4"
    TENANT_ID = "f958e84a-92b8-439f-a62d-4f45996b6d07"
    REDIRECT_URI = "https://cmswebapp-hxanbnh8b6e0fvdf.canadacentral-01.azurewebsites.net/getAToken"

    # Correctly formatted Azure OAuth URL
    AUTH_URL = (
        f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
        f"?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_mode=query"
        f"&scope=openid+profile+email"
        f"&state=12345"
    )

    return redirect(AUTH_URL)

if __name__ == "__main__":
    app.run()
