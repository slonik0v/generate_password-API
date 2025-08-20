from flask import Flask, request, jsonify
import string,random

app = Flask(__name__)

def generate_pass(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/password", methods=["GET"])
def password_endpoint():
    try:
        length = int(request.args.get("length", 12))
        if length < 4:
            return jsonify({"error": "length must be at least 4"}), 400
        pwd = generate_pass(length)
        return jsonify({"password": pwd})
    except ValueError:
        return jsonify({"error": "invalid length parameter"}), 400

if __name__ == "__main__":
    app.run(debug=True)
