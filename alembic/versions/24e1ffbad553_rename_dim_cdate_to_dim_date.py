"""rename dim_cdate to dim_date

Revision ID: 24e1ffbad553
Revises: f088e32af5f2
Create Date: 2024-09-08 14:58:35.722195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24e1ffbad553'
down_revision: Union[str, None] = 'f088e32af5f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table(old_table_name="dim_cdate", new_table_name="dim_date")


def downgrade() -> None:
    op.rename_table(old_table_name="dim_date", new_table_name="dim_cdate")
