from flask import Flask, request, jsonify
from domjudge_builder import build_problem_package

app = Flask(__name__)


@app.route('/')
def hello():
    return "Flask + Traefik is working!"

@app.route('/create-problem', methods=['POST'])
def create_problem():
    data = request.json
    output_path = build_problem_package(data)
    return jsonify({"status": "success", "path": output_path})

if __name__ == '__main__':
    app.run(debug=True)
