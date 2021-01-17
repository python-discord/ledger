"""ensure some fields are not nullable

Revision ID: 1f2ee29c0aab
Revises: 451642c8fcb5
Create Date: 2021-01-17 03:11:48.271239

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1f2ee29c0aab'
down_revision = '451642c8fcb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('issue', 'author',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('issue', 'author_association',
               existing_type=postgresql.ENUM('MEMBER', 'OWNER', 'MANNEQUIN', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE', name='authorassociation'),
               nullable=False)
    op.alter_column('pull_request', 'additions',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pull_request', 'author',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pull_request', 'author_association',
               existing_type=postgresql.ENUM('MEMBER', 'OWNER', 'MANNEQUIN', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE', name='authorassociation'),
               nullable=False)
    op.alter_column('pull_request', 'changed_files',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pull_request', 'deletions',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pull_request', 'status',
               existing_type=postgresql.ENUM('EXPECTED', 'ERROR', 'FAILURE', 'PENDING', 'SUCCESS', name='statuscheckstatus'),
               nullable=False)
    op.alter_column('pull_request', 'total_commits',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pull_request', 'total_commits',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pull_request', 'status',
               existing_type=postgresql.ENUM('EXPECTED', 'ERROR', 'FAILURE', 'PENDING', 'SUCCESS', name='statuscheckstatus'),
               nullable=True)
    op.alter_column('pull_request', 'deletions',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pull_request', 'changed_files',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pull_request', 'author_association',
               existing_type=postgresql.ENUM('MEMBER', 'OWNER', 'MANNEQUIN', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE', name='authorassociation'),
               nullable=True)
    op.alter_column('pull_request', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pull_request', 'additions',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('issue', 'author_association',
               existing_type=postgresql.ENUM('MEMBER', 'OWNER', 'MANNEQUIN', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE', name='authorassociation'),
               nullable=True)
    op.alter_column('issue', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
