"""adding the nickname to user column

Revision ID: 02f1e3727ffb
Revises: 
Create Date: 2025-11-14 17:39:05.930677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02f1e3727ffb'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users',sa.Column('nick_name', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
