from peewee import *


db = SqliteDatabase('Data/FaceID.db')

class Auth(Model):
    class Meta:
        database = db

class User(Auth):
    id_user = PrimaryKeyField(null=False)
    first_name = TextField(null=False)
    last_name = TextField(null=False)
    email = TextField(null=False)
    password = TextField(null=False)

class Images(Auth):
    id_image = PrimaryKeyField(null=False)
    image = BlobField(null=False)

class User_Image(Auth):
    id_user = ForeignKeyField(User, to_field='id_user')
    id_image = ForeignKeyField(Images, to_field='id_image')

db.connect()
db.create_tables([User, Images, User_Image])


def sign_up_db(first_name, last_name, email, password):
    try:
        with db.atomic():
            User.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password)
    except:
        from GUI.Main_Window import error_db
        error_db('Ошибка создания пользователя')

def sign_in_db(email):
    try:
        with db.atomic():
            user = User.get(User.email == email)
            return user.password, user.id_user
    except:
        from GUI.Main_Window import error_db
        error_db('Ошибка при получении пароля пользователя')

def get_id_user(first_name):
    try:
        with db.atomic():
            user = User.get(User.first_name == first_name)
            return user.id_user
    except:
        from GUI.Main_Window import error_db
        error_db('Ошибка при получении id пользователя')

# def photo_to_db(id, shot):
#     try:
#         with db.atomic():
#             Images.create(
#                 image = shot)
#
#             image = Images.get(Images.image == shot)
#             id_img = image.id_image
#
#             User_Image.create(
#                 id_user = id,
#                 id_image = id_img)
#     except:
#         from GUI.Main_Window import error_db
#         error_db()

# def photo_from_db(id):
#     try:
#         with db.atomic():
#             image = Images.get(Images.id_image == id)
#             return image.image
#
#     except:
#         from GUI.Main_Window import error_db
#         error_db()

def info_about_user(id):
    try:
        with db.atomic():
            user = User.get(User.id_user == id)
            return user.first_name, user.last_name, user.email
    except:
        from GUI.Main_Window import error_db
        error_db('Ошибка при получении информации о пользователе')