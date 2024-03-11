# Flask - Flask-Admin Example

This is a basic example of integrating Flask-Admin extension into a Flask application.

`pip install flask-admin`

# To install flask SQLAlchemy

`pip install flask-sqlalchemy`
`pip install --upgrade flask-sqlalchemy`

# Run the Application

Start the Flask development server:

`python3 app.py`

# Accessing Flask-Admin

http://127.0.0.1:5000/admin/

We can access the Flask-Admin interface at above URL endpoint.

# API End Points

- GET /api/users : Get a list of all users.

- GET /api/users/<user_id> : Get details of a specific user.

- POST /api/users : Create a new user.

- PUT /api/users/<user_id> : Update an existing user.

- DELETE /api/users/<user_id> : Delete an existing user.

# CURL to Create a new user

`curl -X POST -H "Content-Type: application/json" -d '{"username": "new_user", "email": "new_user@example.com"}' http://127.0.0.1:5000/api/users`

# CURL to get a list of all users

`curl -X GET http://127.0.0.1:5000/api/users`

# CURL to get details of a specific user

`curl -X GET http://127.0.0.1:5000/api/users/1`

# CURL to update an existing user

`curl -X PUT -H "Content-Type: application/json" -d '{"username": "updated_user", "email": "updated_user@example.com"}' http://127.0.0.1:5000/api/users/1`

# CURL to delete an existing user

`curl -X DELETE http://127.0.0.1:5000/api/users/1`

If you make any changes in model then need to remove db first and start the app again in order to see changes that we made.
Note : This will erase whole schema and create new one

To delete the db
`rm instance/site.db`

Start flask server
`python3 app.py`
