from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
sys.path.append('...')
import utilidades
from BasePage import *

class ListaSessoesPage(BasePage):

    def __init__(self,browser,baseUrl):
        super(ListaSessoesPage,self).__init__(browser, baseUrl)
        pass

    def possui_sessao(self,nomePraia,dia,hora):
        linhaEsperada = "<td>dia hora</td>"
        linhaEsperada = linhaEsperada.replace("dia",dia).replace("hora",hora)
        return linhaEsperada in self.browser.page_source

    