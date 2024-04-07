"""rename department

Revision ID: 5d3d4dbe3c97
Revises: a080e6faeabb
Create Date: 2024-04-07 23:31:54.499369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d3d4dbe3c97'
down_revision = 'a080e6faeabb'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')


def downgrade():
    op.rename_table('departments', 'department')