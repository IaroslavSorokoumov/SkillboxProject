import peewee
from structure_example.config_data.config import DATE_FORMAT
from time import strftime

db = peewee.SqliteDatabase('database.db')
class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = peewee.IntegerField(primary_key=True)
    username = peewee.CharField()
    first_name = peewee.CharField()
    last_name = peewee.CharField(null=True)

class Task(BaseModel):
    task_id = peewee.AutoField()
    user_id = peewee.ForeignKeyField(User, backref='tasks')
    title = peewee.CharField()
    due_date = peewee.DateField()
    is_done = peewee.BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {check} {title} - {due_date}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[]",
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )

def create_models():
    db.create_tables(BaseModel.__subclasses__())