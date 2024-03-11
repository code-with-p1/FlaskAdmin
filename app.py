# app.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
admin = Admin(app, name='flask-admin-example', template_mode='bootstrap3')
api = Api(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Flask-Admin setup for the User model
admin.add_view(ModelView(User, db.session, name='Users', endpoint='users', category='User Management', menu_icon_type='glyph', menu_icon_value='glyphicon-user'))


# Flask-RESTful resource for listing all users
class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

# Flask-RESTful API Resource for User model
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {'id': user.id, 'username': user.username, 'email': user.email}
        else:
            return {'message': 'User not found'}, 404

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        db.session.commit()
        return {'message': 'User updated successfully'}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}

# API endpoints
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
