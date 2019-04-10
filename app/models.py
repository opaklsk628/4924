import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from flask_appbuilder import Model

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name
