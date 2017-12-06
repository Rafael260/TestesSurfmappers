from selenium.webdriver.common.by import By
import time, os, sys
import utilidades
from selenium import webdriver
from LoginPage import *

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://200.17.142.223:6500"
utilidades.acessar(driver,base_url)
paginaLogin = LoginPage(driver)
paginaPrincipal = paginaLogin.fazer_login("oliveira.rafael203@gmail.com","rafaelteste")
paginaBusca = paginaPrincipal.abrir_pagina_busca()
paginaBusca.buscar_praia("Ponta negra")