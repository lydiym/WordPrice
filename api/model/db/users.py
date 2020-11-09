import sqlalchemy

users = sqlalchemy.Table(
    'users',
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(100), unique=True, index=True),
    sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
    sqlalchemy.Column('bch_address', sqlalchemy.String(100))
)
