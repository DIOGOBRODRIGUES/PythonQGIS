#Eu acho que a melhor maneira de ler em um raster para qualquer finalidade com Python / GDAL 
#é usando um scanline ea função de descompactar struct. O código é mais compacto, 
#o controle é mais eficaz eo tempo de execução é mais rápido do que aquele com 'ReadAsArray'. 
#O método scanline / struct depende de fmttypes e seus valores podem ser fornecidos em um dicionário.
# No próximo código eu incluo um exemplo completo de uso para determinar, usando o Python Console Editor 
#do QGIS, a média total e a média por colunas (somente o primeiro valor médio é impresso) para valores 
#de um raster carregado na Visualização de Mapa .

from osgeo import gdal
import struct

layer = iface.activeLayer()
provider = layer.dataProvider()
fmttypes = {'Byte':'B', 'UInt16':'H', 'Int16':'h', 'UInt32':'I', 'Int32':'i', 'Float32':'f', 'Float64':'d'}
path= provider.dataSourceUri()
dataset = gdal.Open(path)
band = dataset.GetRasterBand(1)
totHeight = 0
totColumns = 0
BandType = gdal.GetDataTypeName(band.DataType)
column_means = []

for x in range(band.XSize):
    scanline = band.ReadRaster(x, 0, 1, band.YSize,1, band.YSize, band.DataType)
    values = struct.unpack(fmttypes[BandType] * band.YSize, scanline)

    for value in values:
        totHeight += value
        totColumns += value

    column_means.append(totColumns/float(band.YSize))
    totColumns = 0

average = totHeight / float((band.XSize * band.YSize))
print "Average = %0.5f" % average
print "First mean = %0.5f" % column_means[0]  
dataset = None