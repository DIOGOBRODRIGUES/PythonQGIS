from osgeo import gdal, osr
import os
import struct
import numpy as np

layer = iface.activeLayer()

provider = layer.dataProvider()

path = provider.dataSourceUri()

(raiz,filename) = os.path.split(path)

dataset = gdal.Open(path)

#Get projection
prj = dataset.GetProjection()

#setting band
number_band = 1

band = dataset.GetRasterBand(number_band)

#Get raster metadata
geotransform = dataset.GetGeoTransform()

# Set name of output raster
output_file = "C://Users/diogo/Desktop/testeDeRotina/raster_output.tif"

# Create gtif file with rows and columns from parent raster 
driver = gdal.GetDriverByName("GTiff")

raster = changeRasterValues(band)

dst_ds = driver.Create(output_file, 
                       band.XSize, 
                       band.YSize, 
                       number_band, 
                       band.DataType)

#writting output raster
dst_ds.GetRasterBand(number_band).WriteArray( raster )
.SetNoDataValue(-9999)
#dst_ds.GetRasterBand(number_band).WriteArray( raster )

#setting extension of output raster
# top left x, w-e pixel resolution, rotation, top left y, rotation, n-s pixel resolution
dst_ds.SetGeoTransform(geotransform)

# setting spatial reference of output raster 
srs = osr.SpatialReference(wkt = prj)
dst_ds.SetProjection( srs.ExportToWkt() )

#Close output raster dataset 
dst_ds = None