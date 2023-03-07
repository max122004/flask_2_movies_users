from дз18.dao.model.user import Users


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        users = Users.query.all()
        return users

    def create_user(self, user):
        user_ent = Users(**user)
        self.session.add(user_ent)
        self.session.commit()
        return user_ent