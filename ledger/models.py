from enum import Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum as SQLEnum, Integer, String, DateTime
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean


Base = declarative_base()


class AuthorAssociation(Enum):
    MEMBER = "member"
    OWNER = "owner"
    MANNEQUIN = "mannequin"
    COLLABORATOR = "collaborator"
    CONTRIBUTOR = "contributor"
    FIRST_TIME_CONTRIBUTOR = "first_time_contributor"
    FIRST_TIMER = "first_timer"
    NONE = "none"


class StatusCheckStatus(Enum):
    EXPECTED = "expected"
    ERROR = "error"
    FAILURE = "failure"
    PENDING = "pending"
    SUCCESS = "success"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    issues = relationship("Issue")
    pull_requests = relationship("PullRequest")


class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class IssueMixin:
    number = Column(String, primary_key=True)
    opened = Column(DateTime, nullable=False)
    closed = Column(DateTime)
    labels = Column(postgresql.ARRAY(String), nullable=False, default=[])
    author_association = Column(SQLEnum(AuthorAssociation), nullable=False)


class Issue(Base, IssueMixin):
    __tablename__ = "issue"

    author = Column(ForeignKey("user.id"), nullable=False)


class PullRequest(Base, IssueMixin):
    __tablename__ = "pull_request"

    author = Column(ForeignKey("user.id"), nullable=False)
    changed_files = Column(Integer, nullable=False)
    additions = Column(Integer, nullable=False)
    deletions = Column(Integer, nullable=False)
    total_commits = Column(Integer, nullable=False)
    status = Column(SQLEnum(StatusCheckStatus), nullable=False)
    merged = Column(Boolean)
