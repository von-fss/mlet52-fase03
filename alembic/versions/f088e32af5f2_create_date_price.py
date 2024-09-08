"""create date price

Revision ID: f088e32af5f2
Revises: b3c0d7e31009
Create Date: 2024-09-08 14:52:53.435499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f088e32af5f2'
down_revision: Union[str, None] = 'b3c0d7e31009'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'fac_price',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('open', sa.Numeric),
        sa.Column('high', sa.Numeric),
        sa.Column('low', sa.Numeric),
        sa.Column('close', sa.Numeric),
        sa.Column('inflation', sa.Numeric),
    )


def downgrade() -> None:
    op.drop_table('fac_price')
