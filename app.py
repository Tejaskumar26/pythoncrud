from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config.db import db

#Models
from models.user import User
from models.post import Post
from models.likes import Like
from models.employee import Employee

#ROUTES
from routes.user_routes import user_bp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tejas:2611@localhost/python'
db.init_app(app)

#Routes Register
app.register_blueprint(user_bp,url_prefix='/api')

migrate = Migrate(app, db)

app.config['JWT_SECRET_KEY'] = 'your_secret_key' 
jwt = JWTManager(app)

if __name__ == '__main__':    
 app.run(debug=True,port=3031)


