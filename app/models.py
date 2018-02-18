from sqlalchemy.dialects.mysql import BIGINT, DATETIME, FLOAT, VARCHAR
from app import db


class Base(db.Model):
    __abstract__ = True

    def to_dict(self):
        rv = dict()
        for c in self.__table__.columns:
            rv[c.name] = getattr(self, c.name)
        return rv

    @classmethod
    def generate_dummy(cls, **kwargs):
        d = cls(**kwargs)
        db.session.add(d)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise Exception


class Sentimental(Base):
    __tablename__ = 'sentimentals'
    __table_args__ = ()
    id = db.Column(BIGINT(20), primary_key=True, autoincrement=True)
    sentimental = db.Column(VARCHAR(255))
    mixed = db.Column(FLOAT)
    neutral = db.Column(FLOAT)
    negative = db.Column(FLOAT)
    positive = db.Column(FLOAT)
    created_at = db.Column(DATETIME, server_default=db.func.now())

    def __repr__(self):
        return '<Sentimental %r>' % (self.id)