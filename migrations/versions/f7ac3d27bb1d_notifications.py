"""notifications

Revision ID: f7ac3d27bb1d
Revises: d049de007ccf
Create Date: 2017-11-22 19:48:39.945858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f7ac3d27bb1d"
down_revision = "d049de007ccf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notification",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("timestamp", sa.Float(), nullable=True),
        sa.Column("payload_json", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_notification_name"), "notification", ["name"], unique=False
    )
    op.create_index(
        op.f("ix_notification_timestamp"), "notification", ["timestamp"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_notification_timestamp"), table_name="notification")
    op.drop_index(op.f("ix_notification_name"), table_name="notification")
    op.drop_table("notification")
    # ### end Alembic commands ###
