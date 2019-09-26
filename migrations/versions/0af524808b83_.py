"""empty message

Revision ID: 0af524808b83
Revises: 
Create Date: 2019-09-27 00:02:38.531502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af524808b83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demande_creacompte',
    sa.Column('id_compte', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('nom', sa.String(length=50), nullable=True),
    sa.Column('prenom', sa.String(length=50), nullable=True),
    sa.Column('mail', sa.String(length=50), nullable=True),
    sa.Column('tel', sa.String(length=20), nullable=True),
    sa.Column('adresse', sa.String(length=140), nullable=True),
    sa.Column('justificatif', sa.String(length=20), nullable=True),
    sa.Column('affect', sa.String(length=50), nullable=True),
    sa.Column('valide', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_compte')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('demande_creacompte')
    # ### end Alembic commands ###
