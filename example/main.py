from flask import Flask, request, jsonify
import os
import oauthlib.oauth2
from requests_oauthlib import OAuth2Session

app = Flask(__name__)

# Set up OAuth flow
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")
authorization_base_url = os.environ.get("AUTHORIZATION_URL")
token_url = os.environ.get("TOKEN_URL")

oauth_flow = OAuth2Session(client_id, redirect_uri=redirect_uri)
oauth_flow.scope = ["email", "profile"]

# Set up routes
@app.route("/login", methods=["GET"])
def login():
    authorization_url, state = oauth_flow.authorization_url(authorization_base_url)
    return jsonify({"authorizationUrl": authorization_url})

@app.route("/callback", methods=["GET"])
def callback():
    token = oauth_flow.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)