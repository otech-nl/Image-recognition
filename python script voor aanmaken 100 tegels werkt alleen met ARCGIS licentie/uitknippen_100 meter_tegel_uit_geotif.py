import arcpy
from arcpy.sa import *
import pickle
import numpy as np

arcpy.env.workspace = r"X:/DBA/Databases/IRIS/#2017/machinelearning/TIF"

ML_Y_Raster = Raster('2014_163000_563000_RGB_hrl.tif')

myExtent = ML_Y_Raster.extent

Xmin = myExtent.XMin
Ymin = myExtent.YMin
Xmax = myExtent.XMax
Ymax = myExtent.YMax

xwaarde=Xmin+800
ywaarde=Ymin+370
rasterGrootte=100
Bestandsnaam= str(xwaarde)+'_'+str(ywaarde)+'.tif'
print Bestandsnaam
ClipExtent=str(xwaarde)+' '+str(ywaarde)+' '+str(xwaarde+rasterGrootte)+' '+str(ywaarde+rasterGrootte)
print ClipExtent
arcpy.Clip_management(ML_Y_Raster,ClipExtent,'X:/DBA/Databases/IRIS/#2017/machinelearning/tegels 100x100/'+Bestandsnaam, "#", "#", "NONE")
