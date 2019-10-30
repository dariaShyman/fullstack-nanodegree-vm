from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class LocationCategory(Base):
    __tablename__ = 'location_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Location(Base):
    __tablename__ = 'location'

    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    address = Column(String(250))
    category_id = Column(Integer, ForeignKey('location_category.id'))
    category = relationship(LocationCategory)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'address': self.address,
        }


engine = create_engine('sqlite:///locationData.db')


Base.metadata.create_all(engine)