from flask import Blueprint, request, jsonify
from ..services.user_service import register_user

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = register_user(data['username'], data['email'])
    return jsonify({'id': user.id, 'username': user.username})
