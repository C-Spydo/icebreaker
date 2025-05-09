"""add status and title field to email model

Revision ID: 434a86843003
Revises: 44fca8a51133
Create Date: 2025-03-12 16:36:32.175729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '434a86843003'
down_revision = '44fca8a51133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emails', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('status', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emails', schema=None) as batch_op:
        batch_op.drop_column('status')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
