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
    try:
        payload = {
            "iss": connectedAppClientId,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=30),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": user,
            "scp": ["tableau:views:embed", "tableau:metrics:embed"],
            "Region": "East"
        }

        token = jwt.encode(
            payload,
            connectedAppSecretKey,
            algorithm="HS256",
            headers={
                'kid': connectedAppSecretId,
                'iss': connectedAppClientId
            }
        )
        return token
    except Exception as e:
        print(f"An error occurred while generating the token: {e}")
        return None


@app.route('/')
@app.route('/RegPrice')
def DashBoard_1():
    return render_template("DashBoard_1.html", jwt=get_token())

@app.route('/HW')
def DashBoard_2():
    return render_template("DashBoard_2.html", jwt=get_token())

@app.route('/PrVsFr')
def DashBoard_3():
    return render_template("DashBoard_3.html", jwt=get_token())

@app.route('/COL_Adjusted')
def DashBoard_4():
    return render_template("DashBoard_4.html", jwt=get_token())

@app.route('/Adoption')
def DashBoard_5():
    return render_template("DashBoard_5.html", jwt=get_token())

if __name__ == "__main__":
    app.run(port=8080)
