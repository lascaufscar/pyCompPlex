# -*- coding: utf-8 -*-
"""
/***************************************************************************
 compplex3
                                 A QGIS plugin
 Cálculo de metricas de complexidade em imagens de SR, por ROIs e por imagem
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-06
        copyright            : (C) 2022 by Cláudo Bielenki Jr
        email                : bielenki@ufscar.br
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
    """Load compplex3 class from file compplex3.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Complexidade import compplex3
    return compplex3(iface)
