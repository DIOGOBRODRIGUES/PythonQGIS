from osgeo import gdal
import struct
import numpy as np
from osgeo import gdal
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *


divisor=0

 for layer in iface.mapCanvas().layers():
    file_name = 'C:/Users/diogo/Desktop/AgresteAjustado/' + layer.name() + '.tif'
	divisor = divisor + 1
	ds1 = gdal.Open(fileName, GA_ReadOnly )
	band1 = ds1.GetRasterBand(bandNum1)


	
outFile = "out.tiff"

#Open the dataset
ds1 = gdal.Open(fileName, GA_ReadOnly )
band1 = ds1.GetRasterBand(bandNum1)
band2 = ds1.GetRasterBand(bandNum2)

#Read the data into numpy arrays
data1 = BandReadAsArray(band1)
data2 = BandReadAsArray(band2)

#The actual calculation
dataOut = numpy.sqrt(data1*data1+data2*data2)

#Write the out file
driver = gdal.GetDriverByName("GTiff")
dsOut = driver.Create("out.tiff", ds1.RasterXSize, ds1.RasterYSize, 1, band1.DataType)
CopyDatasetInfo(ds1,dsOut)
bandOut=dsOut.GetRasterBand(1)
BandWriteArray(bandOut, dataOut)

#Close the datasets
band1 = None
band2 = None
ds1 = None
bandOut = None
dsOut = None

