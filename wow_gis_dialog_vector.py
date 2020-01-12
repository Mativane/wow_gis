# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WoWGISDialog
                                 A QGIS plugin
 Import Azorth to your QGIS! 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-12-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Mateusz Ośko 
        email                : osko1996@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wow_gis_dialog_base_vector.ui'))


class WoWGISDialogVector(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WoWGISDialogVector, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.select_all.clicked.connect(self.selectAll)
        self.unselect_all.clicked.connect(self.unselectAll)

    def selectAll(self, state):
        for child in self.groupBox.findChildren(QtWidgets.QCheckBox):
            child.setChecked(True)
    
    def unselectAll(self, state):
        for child in self.groupBox.findChildren(QtWidgets.QCheckBox):
            child.setChecked(False)
