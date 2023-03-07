class UsersService:
    def __init__(self, users_dao):
        self.users_dao = users_dao

    def get_all(self):
        return self.users_dao.get_all()

    def create_user(self, user):
        return self.users_dao.create_user(user)