from flask import Flask, request, session, redirect
import msal
import os

# ----------------------------------------------------
# Flask App Initialization
# ----------------------------------------------------
application = Flask(__name__)       # ✅ keep the name "application"
application.secret_key = "GvnN4QwQN1wKOaa0RlNDS_G3DDvMvXh9tgmevZ24G5A="  # required for session

# ----------------------------------------------------
# Azure AD App Details — UPDATE THESE VALUES
# ----------------------------------------------------
CLIENT_ID = "9277e643-3ae3-4421-b668-7aa47a48acc4 "
CLIENT_SECRET = "18j8Q~iBJ__-RdxpkT.XXXXXXXXXXXXXXXXXX  "
TENANT_ID = "f958e84a-92b8-439f-a62d-4f45996b6d07"
REDIRECT_URI = "https://cmswebapp-hxanbnh8b6e0fvdf.canadacentral-01.azurewebsites.net/getAToken"  # must match Azure portal

# ----------------------------------------------------
# Home Page
# ----------------------------------------------------
@application.route('/')
def home():
    return "Welcome to the Article CMS!"

# ----------------------------------------------------
# Login Route — starts OAuth flow
# ----------------------------------------------------
@application.route('/login')
def login():
    auth_url = (
        f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
        f"?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_mode=query"
        f"&scope=User.Read"
    )
    return redirect(auth_url)

# ----------------------------------------------------
# OAuth Redirect / Callback Route — token is received here
# ----------------------------------------------------
@application.route('/getAToken')
def get_a_token():
    print("OAuth token endpoint reached!")

    code = request.args.get("code")  # get authorization code from URL

    if not code:
        return "No authorization code received."

    # MSAL Confidential Client
    cca = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}"
    )

    # Exchange code for token
    result = cca.acquire_token_by_authorization_code(
        code,
        scopes=["User.Read"],
        redirect_uri=REDIRECT_URI
    )

    if "access_token" in result:
        session["access_token"] = result["access_token"]
        session["user"] = result.get("id_token_claims")
        print("✅ Token retrieved and stored successfully!")
        return redirect("/dashboard")

    return f"❌ Token retrieval failed: {result.get('error_description')}"

# ----------------------------------------------------
# Dashboard Page — where user is redirected after login
# ----------------------------------------------------
@application.route('/dashboard')
def dashboard():
    return "✅ Login successful! Redirected to dashboard."

# ----------------------------------------------------
# Local development — Azure uses gunicorn externally
# ----------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
