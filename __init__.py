# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WoWGIS
                                 A QGIS plugin
 Import Azorth to your QGIS! 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-12-15
        copyright            : (C) 2019 by Mateusz Ośko 
        email                : osko1996@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WoWGIS class from file WoWGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wow_gis import WoWGIS
    return WoWGIS(iface)