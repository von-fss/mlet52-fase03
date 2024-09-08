"""create date table

Revision ID: b3c0d7e31009
Revises: b7025ac9d116
Create Date: 2024-09-08 14:51:56.483489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c0d7e31009'
down_revision: Union[str, None] = 'b7025ac9d116'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'dim_cdate',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(3)),
    )


def downgrade() -> None:
    op.drop_table('dim_date')

