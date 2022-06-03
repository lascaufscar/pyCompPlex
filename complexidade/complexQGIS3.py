import gdal
import os
import numpy as np
import time
from osgeo import gdal_array, ogr
import sys
sys.path.insert(1, 'C:\\Users\\biele\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\processing\\scripts')
from entropia import convolucao


from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingParameterRasterLayer)
import processing
class ComPlexJanus2(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer,
    creates some new layers and returns some results.
    """

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        # Must return a new copy of your algorithm.
        return ComPlexJanus2()

    def name(self):
        """
        Returns the unique algorithm name.
        """
        return 'ComPlexJanus'

    def displayName(self):
        """
        Returns the translated algorithm name.
        """
        return self.tr('ComPlex Janus')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to.
        """
        return self.tr('Complexidade')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs
        to.
        """
        return 'Complexidade'

    def shortHelpString(self):
        """
        Returns a localised short help string for the algorithm.
        """
        return self.tr('Calcula as métricas de complexidade para uma imagem')

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and outputs of the algorithm.
        """
        # 'INPUT' is the recommended name for the main input
        # parameter.
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                'RASTER',
                self.tr('Input raster layer'),
                #types=[QgsProcessing.TypeRaster]
            )
        )

        # 'OUTPUT' is the recommended name for the main output
        # parameter.
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                'SAIDA',
                self.tr('Raster output')
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                'JANELA',
                self.tr('Janela Pixels'),
                defaultValue = 5.0,

            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                'METRICA',
                self.tr('Selecione o tipo de métrica de complexidade'),
                ['He','He/Hmax','SDL','LMC']

            )
        )


    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        Raster = self.parameterAsRasterLayer(parameters,'RASTER', context)
        Janela = self.parameterAsInt(parameters, 'JANELA', context)
        Metrica = self.parameterAsEnum(parameters, 'METRICA', context)
        Saida = self.parameterAsFileOutput(parameters, 'SAIDA', context)
        Tini=time.time()
        NameImagem=str(Raster.source())
        outFN =Saida
        Im=gdal.Open(NameImagem)
        cols=Im.RasterXSize
        rows=Im.RasterYSize
        NrBandas = Im.RasterCount
        kernel=Janela - 2
        opcao=Metrica

        for band in range(NrBandas):
            band +=1
            banda_img=Im.GetRasterBand(band)
            #NoData = banda_img.GetNoDataValue()
            ImArray=banda_img.ReadAsArray().astype(np.float)
            EE=np.array(ImArray)
            ES=convolucao(EE, ImArray, rows, cols, kernel, opcao)
            driver = gdal.GetDriverByName('GTiff')
            outDS = driver.Create(outFN.replace(".tif","")+"_B"+str(band)+".tif", cols, rows, 1, gdal.GDT_Float32)
            outDS.SetGeoTransform(Im.GetGeoTransform())
            outDS.SetProjection(Im.GetProjection())
            outBand = outDS.GetRasterBand(1)
            outBand.WriteArray(ES)
            del(outDS)
            del(EE)
            del(ES)
            del(ImArray)
        del(Im)
        Tfim=time.time()
        print (Tfim-Tini)
        return {}