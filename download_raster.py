import os
from qgis.core import QgsRasterLayer, QgsProject, Qgis
from qgis.utils import iface
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import QSettings

def load_from_wms(layername):
    layername = layername.lower().replace(" ","_")
    uri = "url=http://18.224.109.62:8080/geoserver/wms?request=GetMap&service=WMS&version=1.1.1&layers=wowgis:r_" + layername + "&styles=&crs=EPSG:32662&format=image/geotiff"
    rlayer = QgsRasterLayer(uri, layername, "wms")
    if rlayer.isValid():
        QgsProject.instance().addMapLayer(rlayer)
    else:
        iface.messageBar().pushMessage("Error", "Layer is invaild or connection with geoserver is lost! Please report this issue.", 
            level=Qgis.Critical)


def download_raster(dlgVector):
    checked_checkboxes = []
    for child in dlgVector.groupBox_2.findChildren(QtWidgets.QCheckBox):
        if child.isChecked():
            checked_checkboxes.append(child.text())
    for child in dlgVector.groupBox.findChildren(QtWidgets.QCheckBox):
            if child.isChecked():
                checked_checkboxes.append(child.text())

    for checkbox in checked_checkboxes:
        load_from_wms(checkbox)