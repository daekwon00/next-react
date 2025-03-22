from flask import Flask, request, jsonify
from flask_cors import CORS
from User import get_user_by_id, update_user, list_users, seed_mock_db

app = Flask(__name__)
CORS(app)  # 프론트엔드와의 CORS 이슈 방지

# 초기 데이터 생성
seed_mock_db()

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    """사용자 정보를 가져오는 API"""
    try:
        user_id = int(user_id)
        user = get_user_by_id(user_id)
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({"error": "사용자를 찾을 수 없습니다"}), 404
    except ValueError:
        return jsonify({"error": "잘못된 사용자 ID 형식입니다"}), 400

@app.route('/api/users/<user_id>', methods=['PUT'])
def api_update_user(user_id):
    """사용자 정보를 업데이트하는 API"""
    try:
        user_id = int(user_id)
        data = request.json
        
        try:
            user = update_user(user_id, data)
            return jsonify(user.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
    except ValueError:
        return jsonify({"error": "잘못된 사용자 ID 형식입니다"}), 400

@app.route('/api/users', methods=['GET'])
def api_list_users():
    """모든 사용자 목록을 가져오는 API"""
    users = list_users()
    return jsonify([user.to_dict() for user in users])

if __name__ == '__main__':
    app.run(debug=True, port=5000) 