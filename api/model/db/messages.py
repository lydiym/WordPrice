import sqlalchemy

from .users import users

metadata = sqlalchemy.MetaData()

messages = sqlalchemy.Table(
    'messages',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('owner', sqlalchemy.ForeignKey(users.c.id)),
    sqlalchemy.Column('timestamp', sqlalchemy.TIMESTAMP),
    sqlalchemy.Column("content", sqlalchemy.Text)
)
