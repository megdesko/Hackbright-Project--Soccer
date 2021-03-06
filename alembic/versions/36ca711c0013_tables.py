"""tables

Revision ID: 36ca711c0013
Revises: 463b88fb6ebd
Create Date: 2013-08-03 12:41:25.252651

"""

# revision identifiers, used by Alembic.
revision = '36ca711c0013'
down_revision = '463b88fb6ebd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('season_cycles', u'fee_reseident')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('season_cycles', sa.Column(u'fee_reseident', postgresql.DOUBLE_PRECISION(precision=53), nullable=True))
    ### end Alembic commands ###
