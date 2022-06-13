import os.path


DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'test.db')
FIXTURE_BASE_DIR = 'fixtures'

class Config:
    # Настройки ORM
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Фикстуры
    USER_ROLES_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'user_roles.json')
    USERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'user.json')
    ORDERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'order.json')
    OFFERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'offers.json')