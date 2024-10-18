from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
import random
import string



def generate_random_string(length):
    # Define the characters to choose from: letters and digits
    characters = string.ascii_letters + string.digits
    # Generate a random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string




app = Flask(__name__)
csrf = CSRFProtect(app)
# API route to fetch user data
 
 
@app.route('/api/users/<user_id>', methods=['GET'])
@csrf.exempt # Disable CSRF for this route
def get_user(user_id):
    #current_user = get_jwt_identity()
    #print(current_user)
    #print(has_permission(current_user, 'view_user'))
    # Example usage: generate a random string of length 8
    #random_str = generate_random_string(16)
    random_str = f'str_{user_id}'
    #print(random_str)
    # Code to fetch user data from the database or external APIs
    user_data = {"userId": user_id, "strrand": random_str}
    return jsonify(user_data)
 
 
if __name__ == '__main__':
    app.run()
