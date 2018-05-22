from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def NDVI (banda3, banda4, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'banda3@1'
	raster1.raster = banda3
	raster1.bandNumber = 1
	entries.append(raster1)
	raster2 = QgsRasterCalculatorEntry()
	raster2.ref = 'banda4@1'
	raster2.raster = banda4
	raster2.bandNumber = 1
	entries.append(raster2)
	calc = QgsRasterCalculator ('(banda4@1 + banda3@1) / (banda4@1 - banda3@1)', output, 'GTiff', banda3.extent(), banda3.width(), banda3.height(), entries)
	calc.processCalculation()
	
canvas = qgis.utils.iface.mapCanvas()
NDVI(canvas.layers()[0],canvas.layers()[1], 'C://Users/diogo/Desktop/Nova pasta/evapo.tif')
NDVI(layers[0],layers[1], 'C://Users/diogo/Desktop/Nova pasta/evapo.tif')	