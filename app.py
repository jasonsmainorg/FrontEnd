from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import jwt, uuid , datetime #Interatcion with Tableau
import hashlib #User Password Management

import os

app = Flask(__name__)

connectedAppClientId = os.environ['CONNECTED_APP_CLIENT_ID']
connectedAppSecretId = os.environ['CONNECTED_APP_SECRET_ID']
connectedAppSecretKey = os.environ['CONNECTED_APP_SECRET_KEY']
user = os.environ['TABLEAU_USER']

def get_token():
    return jwt.encode(
        {
            "iss": connectedAppClientId,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=30),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": user,
            "scp": ["tableau:views:embed", "tableau:metrics:embed"],
            "Region": "East"
        },
        connectedAppSecretKey,
        algorithm="HS256",
        headers={
            'kid': connectedAppSecretId,
            'iss': connectedAppClientId
        }
    )

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", jwt=get_token())

if __name__ == "__main__":
    app.run(port=8080)
