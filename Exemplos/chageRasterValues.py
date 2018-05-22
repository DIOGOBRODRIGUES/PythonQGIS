
def changeRasterValues(band):

    fmttypes = {'Byte':'B', 'UInt16':'H', 'Int16':'h', 'UInt32':'I', 'Int32':'i', 'Float32':'f', 'Float64':'d'}

    data_type = band.DataType

    BandType = gdal.GetDataTypeName(band.DataType)

    raster = []

    for y in range(band.YSize):

        scanline = band.ReadRaster(0, y, band.XSize, 1, band.XSize, 1, data_type)
        values = struct.unpack(fmttypes[BandType] * band.XSize, scanline)
        raster.append(values)

    raster = [ list(item) for item in raster ]

    #changing raster values
    for i, item in enumerate(raster):
        for j, value in enumerate(item):
            if value > 160:
                print i, j
                raster[i][j] = 0

    #transforming list in array
    raster = np.asarray(raster)

    return raster