import sqlalchemy

likes = sqlalchemy.Table(
    'likes',
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('owner', sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("message", sqlalchemy.ForeignKey("messages.id"))
)
