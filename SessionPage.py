from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
sys.path.append('...')
import utilidades
from BasePage import *
from HomePage import *

class SessionPage(BasePage):

  def __init__(self,browser,baseUrl):
    super(SessionPage,self).__init__(browser, baseUrl)
    pass

  def preencher_informacoes_session(self,nomePraia,dia,hora):
    utilidades.selecionar_opcao_combobox(self.browser,"id","spots",nomePraia)
    #self.browser.find_element_by_xpath("//select[@id='spots']/option[text()='Areia Preta - Natal/RN']").click()
    utilidades.digitar(self.browser,By.ID,"entryDate",dia + " " + hora)
    pass

  def salvar_session(self):
    utilidades.clicar_no_botao(self.browser,"button","Salvar")
    utilidades.esperar_elemento(self.browser,By.CLASS_NAME,"profile-photo",20)
    pass

  def ir_para_pagina_principal(self):
    utilidades.acessar(self.browser,self.baseUrl)
    return HomePage(self.browser,self.baseUrl)
