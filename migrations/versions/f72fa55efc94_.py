"""empty message

Revision ID: f72fa55efc94
Revises: 
Create Date: 2021-08-05 14:03:16.527685

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f72fa55efc94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=256), nullable=False),
                    sa.Column('password', sa.String(length=128), nullable=False),
                    sa.Column('roll', sa.Integer(), nullable=False),
                    sa.Column('full_name', sa.String(length=256), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
