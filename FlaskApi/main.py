from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user/<user_id>', methods=['GET', 'POST'])
def get_user(user_id):
    if request.method == 'POST':
        data = request.get_json()  # Get the JSON data sent in the POST request
        user = {
            'id': user_id,
            'name': data.get('name', 'John Doe'),  # Default name is 'John Doe' if not provided
            'age': data.get('age', 29)  # Default age is 29 if not provided
        }
        return jsonify(user)
    
    elif request.method == 'GET':
        user = {
            'id': user_id,
            'name': 'John Doe',
            'age': 29
        }
        query = request.args.get('query')
        if query:
            user['query'] = query
        return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)

