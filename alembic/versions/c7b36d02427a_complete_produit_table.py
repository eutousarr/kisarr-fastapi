"""Complete produit table

Revision ID: c7b36d02427a
Revises: e5136ab285fd
Create Date: 2025-07-03 15:16:56.708688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7b36d02427a'
down_revision: Union[str, None] = 'e5136ab285fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
