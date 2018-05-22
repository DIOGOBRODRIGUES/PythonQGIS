#Rotina de calibração da região da Agreste --->surubim---1.2211*layer-68.647
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def Calibracao (imagem, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'imagem@1'
	raster1.raster = imagem
	raster1.bandNumber = 1
	entries.append (raster1)
	calc =QgsRasterCalculator ('1.2211*imagem@1 - 68.647', output, 'GTiff', imagem.extent(), imagem.width(), imagem.height(), entries)
	calc.processCalculation()
	
 for layer in iface.mapCanvas().layers():
    file_name = 'C:/Users/diogo/Desktop/AgresteAjustado/' + layer.name() + '.tif'
    Calibracao(layer, file_name)