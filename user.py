from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic, progress):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.progress = progress

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3], progress=user[4],
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic, progress) "
            "VALUES (?, ?, ?, ?, ?)",
            (id_, name, email, profile_pic, 0),
        )
        db.commit()
    
    @staticmethod
    def update_progress(id, new_progress):
        print(new_progress)
        db = get_db()
        db.execute(
            "UPDATE user "
            "SET progress = (?) "
            "WHERE ID = (?)",
            (new_progress,id),
        )
        db.commit()