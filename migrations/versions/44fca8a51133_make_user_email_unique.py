"""make company name and user email unique

Revision ID: 44fca8a51133
Revises: a0677b7de71a
Create Date: 2025-03-11 12:48:25.188990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44fca8a51133'
down_revision = 'a0677b7de71a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('prospects', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
