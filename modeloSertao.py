#Rotina de calibração da região do Sertão---->Oricuri ---0.7575*layer+15.703
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def Calibracao (imagem, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'imagem@1'
	raster1.raster = imagem
	raster1.bandNumber = 1
	entries.append (raster1)
	calc =QgsRasterCalculator ('0.7575*imagem@1 + 15.703', output, 'GTiff', imagem.extent(), imagem.width(), imagem.height(), entries)
	calc.processCalculation()
	
 for layer in iface.mapCanvas().layers():
    file_name = 'C:/Users/diogo/Desktop/Sertao/' + layer.name() + '.tif'
    Calibracao(layer, file_name)