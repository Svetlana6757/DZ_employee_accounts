"""
Разработай систему управления учетными записями пользователей для небольшой компании.
Компания разделяет сотрудников на обычных работников и администраторов.
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
и могут добавлять или удалять пользователя из системы.
Требования:
1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
ID, имя и уровень доступа ('user' для обычных сотрудников).
2.Класс Admin: Этот класс должен наследоваться от класса User.
Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять
и удалять пользователей из списка (представь, что это просто список экземпляров User).
3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа
и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
"""
class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self._users = []

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
            print(f"Пользователь User {user.get_name()} добавлен")
        else:
            print(f" Пользователь {user.get_name()}уже есть в базе")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"Пользователь {user.get_name()} удален")
        else:
            print("Пользователь {user.get_name()} не найден")

    def list_users(self):
        print("Users list:")
        for user in self._users:
            print(user)


# Пример использования
admin = Admin('001', 'Admin User')
user1 = User('002', 'Игорь Иванов')
user2 = User('003', 'Максим Птеров')

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(user1)
admin.list_users()
