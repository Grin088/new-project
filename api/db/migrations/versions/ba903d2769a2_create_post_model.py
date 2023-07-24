"""create_post_model

Revision ID: ba903d2769a2
Revises: f8c54df2cbf0
Create Date: 2023-07-24 17:43:45.657104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba903d2769a2'
down_revision = 'f8c54df2cbf0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['post_categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_post_categories_id'), 'post_categories', ['id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('rating', sa.Numeric(), nullable=True),
    sa.Column('views', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['post_category_id'], ['post_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_post_categories_id'), table_name='post_categories')
    op.drop_table('post_categories')
    # ### end Alembic commands ###
