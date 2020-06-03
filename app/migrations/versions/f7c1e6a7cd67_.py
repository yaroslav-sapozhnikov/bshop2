"""empty message

Revision ID: f7c1e6a7cd67
Revises: 735f6c93950e
Create Date: 2020-06-03 18:02:50.381978

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f7c1e6a7cd67'
down_revision = '735f6c93950e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('record', 'mobile',
               existing_type=mysql.VARCHAR(collation='utf8_unicode_ci', length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('record', 'mobile',
               existing_type=mysql.VARCHAR(collation='utf8_unicode_ci', length=20),
               nullable=True)
    # ### end Alembic commands ###