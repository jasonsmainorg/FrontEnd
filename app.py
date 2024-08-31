from flask import Flask, render_template, request, url_for, redirect #Hosting the webapp
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user #Session Management
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ['APP_COOKIE_SECRET']

UPLOAD_FOLDER = './static/files/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, email, username, password, files_uploaded):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.files_uploaded = files_uploaded


def get_token():
    return
    # return jwt.encode(
    #     {
    #         "iss": connectedAppClientId,
    #         "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
    #         "jti": str(uuid.uuid4()),
    #         "aud": "tableau",
    #         "sub": user,
    #         "scp": ["tableau:views:embed", "tableau:metrics:embed"],
    #         "Region": "East"
    #     },
    #     connectedAppSecretKey,
    #     algorithm="HS256",
    #     headers={
    #         'kid': connectedAppSecretId,
    #         'iss': connectedAppClientId
    #     }
    # )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('choices'))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)