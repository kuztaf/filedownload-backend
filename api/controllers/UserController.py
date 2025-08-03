class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user(self, user_id):
        return self.user_service.get_user_by_id(user_id)

    def get_users(self):
        return self.user_service.get_all_users()

    def create_user(self, user_data):
        return self.user_service.create_user(user_data)

    def update_user(self, user_id, user_data):
        return self.user_service.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)