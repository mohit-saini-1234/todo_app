from flask import Flask
from flask_mail import Mail, Message


MongoUri = "mongodb+srv://1111111111:1111111111@cluster0.tzzym.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

app = Flask(__name__)
mail = Mail(app)

MAIL_SERVER='smtp.gmail.com'
MAIL_USERNAME = 'mohit_saini@excellencetechnologies.info',
MAIL_PASSWORD = 'pyeyetbwpacvihwp'
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = '465'

api_url = "(<a href ='http://127.0.0.1:5000/set_pass?Email="+str(base64_string)+"'>Click Here To Chnage Password</a>)"
sender_mail = 'mohit_saini@excellencetechnologies.info'
