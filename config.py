import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'OpenID', 'url': ''},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/quickhowto'
#SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost:5432/myapp'
#SQLALCHEMY_ECHO = True

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_FOLDER = 'translations'
LANGUAGES = {
    'en': {'flag': 'gb', 'name': 'English'},
    'pt': {'flag': 'pt', 'name': 'Portuguese'},
    'es': {'flag': 'es', 'name': 'Spanish'},
    'de': {'flag': 'de', 'name': 'German'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'ru': {'flag': 'ru', 'name': 'Russian'}
}


#------------------------------
# GLOBALS FOR GENERAL APP's
#------------------------------
UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'
AUTH_TYPE = 1
#AUTH_LDAP_SERVER = "ldap://dc.domain.net"
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'

#--------------------------------------
# User registration
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
FAB_ADD_SECURITY_VIEWS = False
FAB_ADD_OPENAPI_VIEWS = False
# Config for Flask-WTF Recaptcha necessary for user registration
RECAPTCHA_PUBLIC_KEY = '6LdpQZ4UAAAAAIg6f882Ejs1UozQr0tR7VHCQXxm'
RECAPTCHA_PRIVATE_KEY = '6LdpQZ4UAAAAACQ7edaitzCoaAy62PCniGU2jAay'
# Config for Flask-Mail necessary for user registration

MAIL_PORT=465
MAIL_USE_SSL=False
MAIL_SERVER = '	smtp.mailtrap.io'
MAIL_USE_TLS = True
MAIL_USERNAME = '284ac966676d0e'
MAIL_PASSWORD = '43fbcbfafde49b'
MAIL_DEFAULT_SENDER = 'test111125@gmail.com'
#--------------------------------------

APP_NAME = "Broadway"
APP_THEME = "cyborg.css"  # default
#APP_THEME = "cerulean.css"      #
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"       # black
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"          # good
#APP_THEME = "spacelab.css"      #
#APP_THEME = "united.css"