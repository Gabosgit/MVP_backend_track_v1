"""Updated accommodation table

Revision ID: 96ecf5a603bc
Revises: 7f1f28ef17ec
Create Date: 2025-03-27 00:39:35.013453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96ecf5a603bc'
down_revision: Union[str, None] = '7f1f28ef17ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accommodation', sa.Column('telephone_number', sa.String(length=255), nullable=False))
    op.drop_column('accommodation', 'telephon_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accommodation', sa.Column('telephon_number', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('accommodation', 'telephone_number')
    # ### end Alembic commands ###
