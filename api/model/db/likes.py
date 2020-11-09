import sqlalchemy

from .messages import messages
from .users import users

metadata = sqlalchemy.MetaData()

likes = sqlalchemy.Table(
    'likes',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('owner', sqlalchemy.ForeignKey(users.c.id)),
    sqlalchemy.Column("message", sqlalchemy.ForeignKey(messages.c.id))
)
