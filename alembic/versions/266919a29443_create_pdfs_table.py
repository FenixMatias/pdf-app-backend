"""create pdfs table

Revision ID: 266919a29443
Revises: 
Create Date: 2024-10-24 21:57:36.596962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '266919a29443'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'pdfs',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('file', sa.Text, nullable=False),
        sa.Column('selected', sa.Boolean, nullable=False, default=False)
    )

def downgrade():
    op.drop_table('pdfs')