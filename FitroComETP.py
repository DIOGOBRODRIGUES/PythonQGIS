#faz com que os pixels nulos da etp tambem aparecam na raster da chuva
#as raster dos 12 meses devem estar ordenada como chuva e etp no qgis
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
#filtro de pixels com base em uma camada
def AjusteComETP (chuva, etp, output):
	entries  = []
	raster1 = QgsRasterCalculatorEntry()
	raster1.ref = 'chuva@1'
	raster1.raster = chuva
	raster1.bandNumber = 1
	entries.append(raster1)
	raster2 = QgsRasterCalculatorEntry()
	raster2.ref = 'etp@1'
	raster2.raster = etp
	raster2.bandNumber = 1
	entries.append(raster2)
	calc = QgsRasterCalculator ('(etp@1 > 0) * chuva@1', output, 'GTiff', chuva.extent(), chuva.width(), chuva.height(), entries)
	calc.processCalculation()
	
canvas = qgis.utils.iface.mapCanvas()
mes = 1
camada= 0
while camada < 23 :

	fileName = 'C://Users/diogo/Desktop/Chuva/AjustadaComETP/'+str(mes)+'_p.tif'
	AjusteComETP(canvas.layers()[camada],canvas.layers()[camada+1], fileName)
    camada = camada+2
	mes = mes +1


