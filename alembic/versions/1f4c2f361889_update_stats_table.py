"""update stats table

Revision ID: 1f4c2f361889
Revises: 5708b8779e1c
Create Date: 2013-08-19 01:01:22.154666

"""

# revision identifiers, used by Alembic.
revision = '1f4c2f361889'
down_revision = '5708b8779e1c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('expectation', sa.Float(), nullable=True))
    op.drop_column('team_ratings', u'expectation')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_ratings', sa.Column(u'expectation', postgresql.DOUBLE_PRECISION(precision=53), nullable=True))
    op.drop_column('games', 'expectation')
    ### end Alembic commands ###
