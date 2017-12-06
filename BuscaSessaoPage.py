import sys
sys.path.append('..')
import utilidades
from BasePage import *
from selenium.webdriver.common.by import By

class BuscaSessaoPage(BasePage):

    def __init__(self,browser):
        super(BuscaSessaoPage,self).__init__(browser)
        pass

    def buscar_praia(self,nomePraia):
        utilidades.digitar(self.browser,By.ID,"searchbar_photographer-spot_input",nomePraia)
        utilidades.esperar_elemento(self.browser,By.CLASS_NAME,"searchbar_option",30)
        utilidades.clicar(self.browser,By.CLASS_NAME,"searchbar_option")