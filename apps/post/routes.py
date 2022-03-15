from flask import Blueprint
from apps.post.controller import createPost,getPost



post_bp = Blueprint('post_bp', __name__)
post_bp.route('/createPost', methods=['POST'])(createPost)
post_bp.route('/getPost', methods=['GET'])(getPost)