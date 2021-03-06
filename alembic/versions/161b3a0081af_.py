"""empty message

Revision ID: 161b3a0081af
Revises: 36a845dc80dc
Create Date: 2013-08-14 17:05:47.980538

"""

# revision identifiers, used by Alembic.
revision = '161b3a0081af'
down_revision = '36a845dc80dc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('game_date', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'game_date')
    ### end Alembic commands ###
