import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ma_cle_secrete'

    # init SQLAlchemy
    SQLALCHEMY_DATABASE_URI =(os.environ.get('DATABASE_URL') or
                              'sqlite:///' + os.path.join(basedir, 'test\\app.db')) + '?check_same_thread=False'
    # 'mysql://root:test@localhost:3306/gestibank'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
