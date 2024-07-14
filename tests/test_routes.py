import unittest
from app import create_app, db
from app.models import User, Post

class TestBlogAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation_with_existing_email(self):
        response = self.client.post('/signup', json={'username': 'testuser', 'password': 'anotherpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', response.get_json().get('error'))

    def test_user_creation_with_no_password(self):
        response = self.client.post('/signup', json={'username': 'newuser'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing username or password', response.get_json().get('error'))

    def test_user_creation_with_no_email(self):
        response = self.client.post('/signup', json={'password': 'newpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing username or password', response.get_json().get('error'))

    def test_user_creation_with_empty_request(self):
        response = self.client.post('/signup', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing username or password', response.get_json().get('error'))

    def test_user_login_with_invalid_password(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Unauthorized', response.get_json().get('error'))

    def test_user_login_with_invalid_email(self):
        response = self.client.post('/login', json={'username': 'nonexistentuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Unauthorized', response.get_json().get('error'))

    def test_signup(self):
        response = self.client.post('/signup', json={'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
        auth_header = {'Authorization': 'Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk'}
        response = self.client.post('/posts', json={'title': 'Test Post', 'content': 'This is a test post.'}, headers=auth_header)
        self.assertEqual(response.status_code, 201)

    def test_get_posts(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)

    def test_get_post(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.status_code, 404)  # Since no post exists initially

if __name__ == '__main__':
    unittest.main()
