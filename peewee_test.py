
from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('test_database.db')

class User(Model):
    name = CharField(max_length=100)
    age = IntegerField()

    class Meta:
        database = db

db.create_tables([User])

user1 = User(
    name='Dmitry',
    age=25
)
user1.save()

user2 = User(
    name='Alex',
    age=35
)
user2.save()

users = User.select()
for user in users:
    print(
        "name: ", user.name, '// '
        "age: ", user.age, '\n'
    )

retrieved_user = User.get(User.id == 1)
print(retrieved_user.name)
retrieved_user.name = 'Дмитрий'
retrieved_user.save()

user2.delete_instance()
