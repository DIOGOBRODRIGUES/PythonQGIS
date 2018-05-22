#Estatistica utilizando o numpy

from osgeo import gdal
import struct
import numpy as np
layer = iface.activeLayer()
provider = layer.dataProvider()
fmttypes = {'Byte':'B', 'UInt16':'H', 'Int16':'h', 'UInt32':'I', 'Int32':'i', 'Float32':'f', 'Float64':'d'}
path= provider.dataSourceUri()
dataset = gdal.Open(path)
band = dataset.GetRasterBand(1)

BandType = gdal.GetDataTypeName(band.DataType)

scanline = band.ReadRaster(5, 7, 3, 3, 3, 3, band.DataType)
values = struct.unpack(fmttypes[BandType] * 9, scanline)

print values
print "mean = ", np.mean(values)
print "median = ", np.median(values)
print "min = ", np.min(values)
print "max = ", np.max(values)

dataset = None