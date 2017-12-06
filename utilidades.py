# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os
import sys

def acessar(driver, url):
	driver.get(url)

def logar(driver, usuario, senha):
	clicar(driver,By.LINK_TEXT,"Entrar")
	esperar_elemento(driver,By.ID,"btn-login",30)
	digitar(driver,By.NAME,"email",usuario)
	digitar(driver,By.NAME,"password",senha)
	clicar(driver,By.ID,"btn-login")
	esperar_elemento(driver,By.LINK_TEXT,"Vender Fotos", 60)
	pass

def sair(driver):
	acessar(driver,"http://200.17.142.223:6500/logout")
	pass


def esperar_elemento(driver, maneiraProcura, elemento, tempoLimite):
	WebDriverWait(driver, tempoLimite).until(
        EC.presence_of_element_located((maneiraProcura, elemento)))
	time.sleep(2)

def encontrar_elemento(driver, maneiraProcura, elemento):
	return driver.find_element(maneiraProcura,elemento)

def encontrar_elementos(driver, elemento, maneiraProcura):
	return driver.find_elements(maneiraProcura,elemento)

def clicar(driver, maneiraProcura, elemento):
	elemento = encontrar_elemento(driver, maneiraProcura, elemento)
	if (elemento != None):
		elemento.click()

def digitar(driver, maneiraProcura, elemento, texto):
	elemento = encontrar_elemento(driver,maneiraProcura,elemento)
	if (elemento != None):
		elemento.clear()
		elemento.send_keys(texto)

def get_diretorio_atual():
	return os.path.dirname(os.path.abspath(__file__))

def read(filename, encoding='utf-8', errors='strict'):
    with open(filename, 'rb') as f:
        return f.read().decode(encoding, errors=errors)

def get_parametros_script(nomeScript):
	nomeArquivoParametros = nomeScript.replace(".py","") + "_parametros.txt"
	diretorioAtual = get_diretorio_atual()
	conteudo = read(diretorioAtual + "\\" + nomeArquivoParametros)
	linhas = conteudo.split("\n")
	parametros = {}
	for linha in linhas:
		divisaoParametro = linha.split('=')
		if (len(divisaoParametro) > 1):
			parametros[divisaoParametro[0]] = divisaoParametro[1]

	return parametros

def inicializar_diretorio_prints(nomeScript):
	nomePasta = get_diretorio_pasta_prints(nomeScript)
	#Se a pasta nao existe ainda, cria
	if (not os.path.isdir(nomePasta)):
		os.mkdir(nomePasta)
	#Se ja existe, apaga os prints que ja existem
	else:
		prints = os.listdir(nomePasta)
		for file in prints:
			os.remove(nomePasta + '\\'+ file)

def get_diretorio_pasta_prints(nomeScript):
	diretorioAtual = get_diretorio_atual()
	return diretorioAtual + '\\Documentos\\'+ nomeScript.replace(".py","") + "_prints"

descricoes_prints = []

def tirar_print(driver,nomeScript,descricao):
	nomePasta = get_diretorio_pasta_prints(nomeScript) 
	numeroPrint = len(os.listdir(nomePasta)) + 1
	nomePrint = nomeScript.replace(".py","") + "_print_" + str(numeroPrint)
	#driver.get_screenshot_as_file(nomePasta +'/' + nomePrint + '.png')
	driver.save_screenshot(nomePasta +'/' + nomePrint + '.jpg')
	descricoes_prints.append(descricao)