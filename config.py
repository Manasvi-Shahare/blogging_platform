import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5433/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False