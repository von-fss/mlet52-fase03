"""create country table

Revision ID: b7025ac9d116
Revises: 
Create Date: 2024-09-08 14:44:47.864382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7025ac9d116'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'dim_country',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('iso3', sa.String(3)),
        sa.Column('name', sa.String(50)),
        sa.Column('currency', sa.String(3))        
    )


def downgrade() -> None:
    op.drop_table('dim_country')
