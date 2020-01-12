import os
from qgis.core import QgsVectorLayer, QgsProject, Qgis
from qgis.utils import iface
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import QSettings

def load_from_wfs(layername):
    layername = layername.lower().replace(" ","_")
    uri = "http://18.224.109.62:8080/geoserver/wfs?srsname=EPSG:32662&typename=wowgis:v_" + layername + "&version=1.1.0&request=GetFeature&service=WFS"
    vlayer = QgsVectorLayer(uri, layername, "WFS")
    if vlayer.isValid():
        QgsProject.instance().addMapLayer(vlayer)
    else:
        iface.messageBar().pushMessage("Error", "Layer is invaild or connection with geoserver is lost! Please report this issue.", 
            level=Qgis.Critical)

def download_vector(dlgVector):
    checked_checkboxes = []
    for child in dlgVector.groupBox.findChildren(QtWidgets.QCheckBox):
            if child.isChecked():
                checked_checkboxes.append(child.text())
    for child in dlgVector.groupBox_2.findChildren(QtWidgets.QCheckBox):
            if child.isChecked():
                checked_checkboxes.append(child.text())

    for checkbox in checked_checkboxes:
        load_from_wfs(checkbox)