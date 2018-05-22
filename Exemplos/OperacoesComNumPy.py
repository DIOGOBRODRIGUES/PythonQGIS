from osgeo import gdal
import struct
import numpy as np

layer = iface.activeLayer()
provider = layer.dataProvider()
fmttypes = {'Byte':'B', 'UInt16':'H', 'Int16':'h', 'UInt32':'I', 'Int32':'i', 'Float32':'f', 'Float64':'d'}
path= provider.dataSourceUri()
dataset = gdal.Open(path)
#band = dataset.GetRasterBand(1)
data1 = dataset.GetRasterBand(1)
totHeight = 0
totColumns = 0
coluna = 0
pixels =0
#BandType = gdal.GetDataTypeName(band.DataType)
BandType = gdal.GetDataTypeName(data1.DataType)
column_means = []
raster = []


for x in range(band.XSize):
    scanline = band.ReadRaster(x, 0, 1, band.YSize,1, band.YSize, band.DataType)
    values = struct.unpack(fmttypes[BandType] * band.YSize, scanline)
   
    
    for value in values:
        if value > 0:
            raster.append(value)
            totHeight += value
            totColumns += value
            coluna = coluna + 1 
            pixels = pixels+1
        #else:
            #coluna = coluna - 1
            #pixels = pixels - 1

    column_means.append(totColumns/coluna)
    totColumns = 0
    coluna=1

average = totHeight / pixels
print "Average = %0.5f" % average
print "First mean = %0.5f" % column_means[0] 
print "coluna=%i" %coluna
print "pixels = %i " %pixels
print "mean = ", np.mean(raster)