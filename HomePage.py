from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
import utilidades
from BasePage import *
from LoginPage import *
from BuscaSessaoPage import *

class HomePage(BasePage):

	def __init__(self,browser, baseUrl):
		super(HomePage,self).__init__(browser,baseUrl)
		pass

	def abrir_pagina_busca(self):
		utilidades.clicar(self.browser,By.LINK_TEXT,"Encontre sua Foto")
		utilidades.esperar_elemento(self.browser,By.ID,"searchbar_search_btn",30)
		return BuscaSessaoPage(self.browser,self.baseUrl)

	def sair_do_sistema(self):
		utilidades.sair(self.browser)
		return LoginPage(self.browser,self.baseUrl)
