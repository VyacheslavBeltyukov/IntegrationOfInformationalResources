from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Create a new user in the database
@app.route('/users', methods=['POST'])
def create_user():
    # Get the user data from the request body
    data = request.get_json()
    name = data['name']
    email = data['email']

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Insert the new user into the database
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

    # Close the database connection
    conn.close()

    # Return a response with the new user's ID
    return jsonify({'id': c.lastrowid})


# Get all users from the database
@app.route('/users', methods=['GET'])
def get_users():
    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Select all users from the database
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    # Convert the rows to a list of dictionaries
    users = []
    for row in rows:
        user = {'id': row[0], 'name': row[1], 'email': row[2]}
        users.append(user)

    # Close the database connection
    conn.close()

    # Return a response with the list of users
    return jsonify(users)


# Get a single user from the database by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Select the user from the database by ID
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = c.fetchone()

    # If the user is not found, return a 404 error
    if row is None:
        return jsonify({'error': 'User not found'}), 404

    # Convert the row to a dictionary
    user = {'id': row[0], 'name': row[1], 'email': row[2]}

    # Close the database connection
    conn.close()

    # Return a response with the user data
    return jsonify(user)


# Update a user in the database by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Get the user data from the request body
    data = request.get_json()
    name = data['name']
    email = data['email']

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Update the user in the database by ID
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
    conn.commit()

    # If the user is not found, return a 404 error
    if c.rowcount == 0:
        return jsonify({'error': 'User not found'}), 404

    # Close the database connection
    conn.close()

    # Return a response
    return jsonify({'Success': f'User with id {user_id} was updated'})


# Delete a user in the database by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Update the user in the database by ID
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()

    # If the user is not found, return a 404 error
    if c.rowcount == 0:
        return jsonify({'error': 'User not found'}), 404

    # Close the database connection
    conn.close()

    # Return a response
    return jsonify({'Success': f'User with id {user_id} was deleted from db'})

    # Return
