import sys
sys.path.append('..')
sys.path.append('...')
import utilidades
from BasePage import *
from HomePage import *

class LoginPage(BasePage):

	def __init__(self,browser):
		super(LoginPage,self).__init__(browser)

	def fazer_login(self,usuario,senha):
		utilidades.logar(self.browser,usuario,senha)
		return HomePage(self.browser)
		