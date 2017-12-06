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
	pass

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
	pass

def esperar_elemento_visivel(driver, maneiraProcura, elemento, tempoLimite):
	WebDriverWait(driver, tempoLimite).until(
        EC.visibility_of_element_located((By.CLASS_NAME,"searchbar_option")))
	time.sleep(1)
	pass

def encontrar_elemento(driver, maneiraProcura, elemento):
	return driver.find_element(maneiraProcura,elemento)

def encontrar_elementos(driver, elemento, maneiraProcura):
	return driver.find_elements(maneiraProcura,elemento)

def clicar(driver, maneiraProcura, elemento):
	elemento = encontrar_elemento(driver, maneiraProcura, elemento)
	if (elemento != None):
		elemento.click()
	pass

def digitar(driver, maneiraProcura, elemento, texto):
	elemento = encontrar_elemento(driver,maneiraProcura,elemento)
	if (elemento != None):
		elemento.clear()
		elemento.send_keys(texto)
	pass

def coletar_nome_para_url(nome,separador):
	return nome.lower().replace(" ", separador)

def selecionar_opcao_combobox(driver,procuraSelect,elementoCb,selecionado):
	expressaoXpath = "//select[@procuraSelect='elementoCb']/option[text()='selecionado']"
	expressaoXpath = expressaoXpath.replace("procuraSelect",procuraSelect).replace("elementoCb",elementoCb).replace("selecionado",selecionado)
	driver.find_element_by_xpath(expressaoXpath).click()
	pass

def clicar_no_botao(driver,tipoElementoHtml,textoBotao):
	expressaoXpath =  "//tipoElementoHtml[contains(text(), 'textoBotao')]"
	expressaoXpath = expressaoXpath.replace("tipoElementoHtml", tipoElementoHtml).replace("textoBotao",textoBotao)
	driver.find_element_by_xpath(expressaoXpath).click()
	pass