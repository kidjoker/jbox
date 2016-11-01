"""empty message

Revision ID: eb4f45fc11c1
Revises: 9b92ed8d4d8d
Create Date: 2016-10-28 10:56:14.093373

"""

# revision identifiers, used by Alembic.
revision = 'eb4f45fc11c1'
down_revision = '9b92ed8d4d8d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authorizations', sa.Column('type', sa.String(length=50), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authorizations', 'type')
    ### end Alembic commands ###