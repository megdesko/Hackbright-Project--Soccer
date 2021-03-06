"""empty message

Revision ID: 5708b8779e1c
Revises: e357d331c94
Create Date: 2013-08-19 00:49:54.203528

"""

# revision identifiers, used by Alembic.
revision = '5708b8779e1c'
down_revision = 'e357d331c94'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_ratings', sa.Column('expectation', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team_ratings', 'expectation')
    ### end Alembic commands ###
