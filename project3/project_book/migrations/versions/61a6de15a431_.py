"""empty message

Revision ID: 61a6de15a431
Revises: 
Create Date: 2021-06-01 19:26:38.906379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61a6de15a431'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bestsell',
    sa.Column('sell_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=False),
    sa.Column('imageLink', sa.String(length=128), nullable=True),
    sa.Column('which', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('sell_id')
    )
    op.create_table('bookmylist',
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('author', sa.String(length=256), nullable=True),
    sa.Column('price', sa.String(length=256), nullable=True),
    sa.Column('discount', sa.String(length=256), nullable=True),
    sa.Column('publisher', sa.String(length=256), nullable=True),
    sa.Column('isbn', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('pubdate', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('isbn')
    )
    op.create_table('comparelist',
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('link', sa.String(length=256), nullable=True),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('author', sa.String(length=256), nullable=True),
    sa.Column('price', sa.String(length=256), nullable=True),
    sa.Column('discount', sa.String(length=256), nullable=True),
    sa.Column('publisher', sa.String(length=256), nullable=True),
    sa.Column('isbn', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('pubdate', sa.String(length=256), nullable=True),
    sa.Column('embedding', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comparelist')
    op.drop_table('bookmylist')
    op.drop_table('bestsell')
    # ### end Alembic commands ###
