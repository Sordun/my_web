"""added email to user

Revision ID: 1db6e2f9ee8a
Revises: 6e9adb20ff8e
Create Date: 2020-01-21 13:54:02.896581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1db6e2f9ee8a'
down_revision = '6e9adb20ff8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
