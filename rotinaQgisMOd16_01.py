#Rotina para multiplar por 0.1 todas as imagens abertas do MOD16 no QGIS
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def Evapo (imagem, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'imagem@1'
	raster1.raster = imagem
	raster1.bandNumber = 1
	entries.append (raster1)
	calc =QgsRasterCalculator ('imagem@1 * 0.1', output, 'GTiff', imagem.extent(), imagem.width(), imagem.height(), entries)
	calc.processCalculation()
	
 for layer in iface.mapCanvas().layers():
    file_name = 'C://Users/diogo/Desktop/Nova pasta/' + layer.name() + '.tif'
    Evapo(layer, file_name)	

