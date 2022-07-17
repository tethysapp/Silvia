from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry



Base = declarative_base()



class FloodExtent(Base):
    """
    SQLAlchemy table definition for storing flood extent polygons.
    """
    __tablename__ = 'flood_extents'

    # Columns
    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON'))
    comid = Column(Integer)
    flood = Column(Integer)

    def __init__(self, wkt, comid):
        """
        Constructor
        """
        # Add Spatial Reference ID
        self.geom = 'SRID=4326;{0}'.format(wkt)
        self.comid = comid
        self.flood = 1