import sys
sys.path.append('..')
sys.path.append('...')
import utilidades

class BasePage:
	def __init__(self, browser):
		self.browser = browser
		pass

	def acessar(self,url):
		utilidades.acessar(self.browser,url)
		pass