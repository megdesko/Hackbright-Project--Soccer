from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=64)),
    Column('lastname', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=64)),
    Column('address', String(length=120)),
    Column('city', String(length=64)),
    Column('state', String(length=64)),
    Column('zipcode', String(length=64)),
    Column('country', String(length=64)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('dob', DateTime),
    Column('gender', String(length=64)),
    Column('fitness', SmallInteger),
    Column('experience', Integer),
    Column('willing_teamLeader', Boolean, default=ColumnDefault(False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].drop()