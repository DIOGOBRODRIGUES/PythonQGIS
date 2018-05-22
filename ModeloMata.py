#Rotina de calibração da região da Zona da Mata MATA--> Recife---- -0.9614*layer-65.706
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def Calibracao (imagem, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'imagem@1'
	raster1.raster = imagem
	raster1.bandNumber = 1
	entries.append (raster1)
	calc =QgsRasterCalculator ('0.9614*imagem@1 - 65.706', output, 'GTiff', imagem.extent(), imagem.width(), imagem.height(), entries)
	calc.processCalculation()
	
 for layer in iface.mapCanvas().layers():
    file_name = 'C:/Users/diogo/Desktop/MataAjustado/' + layer.name() + '.tif'
    Calibracao(layer, file_name)