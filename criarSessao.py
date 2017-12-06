from selenium.webdriver.common.by import By
import time, os, sys
import utilidades
from selenium import webdriver
from LoginPage import *

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://200.17.142.223:6500"
utilidades.acessar(driver,base_url)
paginaLogin = LoginPage(driver,base_url)
paginaPrincipal = paginaLogin.fazer_login("oliveira.rafael203@gmail.com","rafaelteste")
paginaSessao = paginaPrincipal.abrir_pagina_criar_session()
paginaSessao.preencher_informacoes_session("Areia Preta - Natal/RN","16/12/2017","17:35")
paginaSessao.salvar_session()
time.sleep(5)
driver.quit()