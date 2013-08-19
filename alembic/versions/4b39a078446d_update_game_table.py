"""update game table

Revision ID: 4b39a078446d
Revises: 224d2bf548e8
Create Date: 2013-08-16 09:57:08.804895

"""

# revision identifiers, used by Alembic.
revision = '4b39a078446d'
down_revision = '224d2bf548e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('away_loss', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('away_tie', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('away_win', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('home_loss', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('home_tie', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('home_win', sa.Integer(), nullable=True))
    op.drop_column('team_ratings', u'team_tie')
    op.drop_column('team_ratings', u'team_win')
    op.drop_column('team_ratings', u'team_loss')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_ratings', sa.Column(u'team_loss', sa.INTEGER(), nullable=True))
    op.add_column('team_ratings', sa.Column(u'team_win', sa.INTEGER(), nullable=True))
    op.add_column('team_ratings', sa.Column(u'team_tie', sa.INTEGER(), nullable=True))
    op.drop_column('games', 'home_win')
    op.drop_column('games', 'home_tie')
    op.drop_column('games', 'home_loss')
    op.drop_column('games', 'away_win')
    op.drop_column('games', 'away_tie')
    op.drop_column('games', 'away_loss')
    ### end Alembic commands ###