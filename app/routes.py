from flask import Blueprint, request, jsonify
from .models import Post, db
from . import auth

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return jsonify(message="Welcome to the Simple Blogging Platform!"), 200

@bp.route('/posts', methods=['POST'])
@auth.login_required
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({'error': 'Missing title or content'}), 400

    post = Post(title=title, content=content, user_id=auth.current_user().id)
    db.session.add(post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully'}), 201

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

@bp.route('/posts/<int:id>', methods=['PUT'])
@auth.login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id != auth.current_user().id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()

    return jsonify({'message': 'Post updated successfully'})

@bp.route('/posts/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id != auth.current_user().id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({'message': 'Post deleted successfully'})
