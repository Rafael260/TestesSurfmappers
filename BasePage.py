import sys
sys.path.append('..')
sys.path.append('...')
import utilidades

class BasePage:
	def __init__(self, browser, baseUrl):
		self.browser = browser
		self.baseUrl = baseUrl
		pass

	def acessar(self,url):
		utilidades.acessar(self.browser,url)
		pass