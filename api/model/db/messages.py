import sqlalchemy

messages = sqlalchemy.Table(
    'messages',
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('owner', sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column('timestamp', sqlalchemy.TIMESTAMP),
    sqlalchemy.Column("content", sqlalchemy.Text)
)
