"""update user table

Revision ID: 4b692e5a8ec9
Revises: 55d784935c02
Create Date: 2013-08-06 12:02:29.801632

"""

# revision identifiers, used by Alembic.
revision = '4b692e5a8ec9'
down_revision = '55d784935c02'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###