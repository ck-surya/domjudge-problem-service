from flask import Flask, request, jsonify
from domjudge_builder import build_problem_package  # 🔁 FIXED this import

app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask + Traefik is working!"

@app.route('/create-problem', methods=['POST'])
def create_problem():
    try:
        data = request.get_json()
        output_path = build_problem_package(data)
        return jsonify({"status": "success", "path": output_path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Bind to all interfaces (important for Docker)
    app.run(host='0.0.0.0', port=5000, debug=True)
