# Put your persistent store initializer functions in here
import os
from sqlalchemy.orm import sessionmaker
from .model import Base, FloodExtent

from requests import Request
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement

def init_flooded_addresses_db(engine,first_time):
	"""
	Initialize the flooded addresses database.
	"""
	# STEP 1: Create database tables
	Base.metadata.create_all(engine)
	# STEP 2: Add data to the database
	if first_time:
		print("initializing database")
		# Find path of parent directory relative to this file
		
		# Create a session object in preparation for interacting with the database
		SessionMaker = sessionmaker(bind=engine)
		session = SessionMaker()

		url = 'https://geoserver.hydroshare.org/geoserver/HS-22714855232d44198d12aa4109ec8478/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=HS-22714855232d44198d12aa4109ec8478:GEOGLOWS_SilviaV3&outputFormat=application/json'

		q = Request('GET', url).prepare().url
		df = gpd.read_file(q, format='GML')
		df.crs = 'EPSG:4326'
		df['geom'] = df['geometry'].apply(lambda x: WKTElement(x.wkt, srid=4326))
		df.drop('geometry', 1, inplace=True)

		dest = gpd.GeoDataFrame(columns=['comid', 'geom'], geometry='geom')
		dest['geom'] = df['geom']
		dest['comid'] = df['COMID']
		dest['flood'] = 1

		print(df)
		dest.to_sql('flood_extents', engine, if_exists='append', index=False, 
                         dtype={'geom': Geometry('MULTIPOLYGON', srid= 4326)})

	
		session.commit()

		# Close the connection to prevent issues
		session.close()


		



