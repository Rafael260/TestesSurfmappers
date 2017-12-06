import sys
sys.path.append('..')
import utilidades
from BasePage import *
from selenium.webdriver.common.by import By
import time

class BuscaSessaoPage(BasePage):

    def __init__(self,browser,baseUrl):
        super(BuscaSessaoPage,self).__init__(browser,baseUrl)
        pass

    def buscar_praia(self, estado, nomePraia):
        estadoUrl = utilidades.coletar_nome_para_url(estado,"-")
        nomePraiaUrl = utilidades.coletar_nome_para_url(nomePraia,"_")
        utilidades.acessar(self.browser,self.baseUrl+"/album/list?country=brazil&state=" + estadoUrl + "&spot=" + nomePraiaUrl)
        pass

    def possui_resultados(self):
        try:
            utilidades.esperar_elemento(self.browser,By.PARTIAL_LINK_TEXT,"Ponta Negra",10)
            return True
        except:
            return False