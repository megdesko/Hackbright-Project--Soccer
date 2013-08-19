"""Change dob type to Date

Revision ID: 23eb81f2e3c2
Revises: 1a9a914e86fa
Create Date: 2013-08-08 16:39:17.810203

"""

# revision identifiers, used by Alembic.
revision = '23eb81f2e3c2'
down_revision = '1a9a914e86fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dob', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dob')
    ### end Alembic commands ###