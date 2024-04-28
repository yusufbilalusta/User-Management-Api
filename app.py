from flask import Flask, jsonify, request

app = Flask(__name__)
#User olustururken id bilgisi eklenmelidir
# Dummy user data
users = []

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify(data), 201

@app.route("/get-user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user.get("id") == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route("/update-user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user.get("id") == user_id:
            user.update(data)
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route("/delete-user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for index, user in enumerate(users):
        if user.get("id") == user_id:
            users.pop(index)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404

@app.route("/list-users", methods=["GET"])
def list_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
