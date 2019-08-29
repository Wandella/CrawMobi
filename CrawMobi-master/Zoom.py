import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

class zoom:
	
	"""docstring for zoom"""
	
	def __init__(self, aparelho):
		super(zoom, self).__init__()
		self.aparelho = aparelho

	def preçoZoom(self):
		print("Entrando no site")
		link_preço = 'https://www.zoom.com.br/celular' #site alternativo para aquisição dos preços em reais
		
		# Abrindo o navegador para realização da pesquisa do smartphone
		driver = webdriver.Chrome('/home/wandella/Documentos/CrawMobi/CrawMobi-master/chromedriver')
		driver.get(link_preço)
		WebDriverWait(driver, 3)
		

		#Funções utilizadas na execução
		def precoFinal(preço): # Faz as alterações exatas no preço em Real
			print("Transformar preço")
			preço = preço.split(' ')[1]
			preço = preço.replace('.','')
			preço = preço.replace(',','.')
			preço = float(preço)
			print("Ponto para retorno")
			return preço

		# As funções a seguir escolhem o modal correto dentro do site Zoom a partir do nome do aparelho

		def escolheCard(aparelho, driver): # Comparação do nome para escolha correta, do card, no site Zoom
			
			print("Função de escolher o card -> ",aparelho)
			
			pesquisado1 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]/h2/a').text
			print("Celular pesquisado ->",pesquisado1)
			pesquisado1 = pesquisado1.upper()
			print("Pesquisado",pesquisado1,"aparelho",aparelho)
			
			if pesquisado1.find(aparelho)>-1:
				#driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]').click()
				#Preço = driver.find_element_by_xpath('//*[@id="productInfo"]/div/div[2]/p/span[2]/a/strong').text #Kimovil
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[3]/span[2]/a[1]').text #Kimovil
				print(Preço)
				return Preço

			else:
				pesquisado2 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]/h2/a').text
				pesquisado2 = pesquisado2.upper()
				
			if pesquisado2.find(aparelho)>-1:
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[3]/span[2]/a[1]').text #Kimovil
				return Preço
			else:
				pesquisado3 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[2]/h2').text
				pesquisado3 = pesquisado3.upper()

			if pesquisado3.find(aparelho)>-1:
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[3]/span[2]/a[1]').text #Kimovil
				return Preço
			else:
				pesquisado4 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[2]/h2').text
				pesquisado4 = pesquisado3.upper()

			if pesquisado4.find(aparelho)>-1:
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[3]/span[2]/a[1]').text #Kimovil
				return Preço
			elif Preço == '':
				print("Ultimo Caso",Preço)
				Preço = driver.find_element_by_xpath('//*[@id="productInfo"]/div/div[2]/p/span[2]/a/strong/text()').text #Kimovil
				return Preço
			else:
				return None
			
		# Função que complementa a função escolheCard(), vendo de qual marca é o aparelho para comparação
		def completaEscolheCard(aparelho):
			print("Zoom completando card")
			if aparelho.find("(")>-1:
				aparelho = aparelho.split("(")[0]

			if aparelho.find("+")>-1:
				aparelho = aparelho.replace("+"," PLUS")

			if aparelho.find('APPLE')>-1:
				var = aparelho.replace("APPLE", "")
				return var

			elif aparelho.find('MOTOROLA')>-1:
				var = aparelho.replace("MOTOROLA", "")
				var = var.replace("MOTO G", "MOTO G G")
				var = var.replace("MOTO Z", "MOTO Z Z")
				var = var.replace("ONE","MOTOROLAONE")
				return var
			elif aparelho.find('SAMSUNG')>-1:
				var = var.replace("SAMSUNG", "")
				return var
			else:
				return aparelho
				
			""" elif aparelho.find('XIAOMI')>-1:
				var = aparelho.replace("XIAOMI", "")
				return var """
			""" if (aparelho.split(' ')[0] == 'MOTOROLA'):
				if ((len(pesquisado) - (len(aparelho)+11+5+7+2)) < 2):
					return True
				else:
					return False
			
			if (aparelho.split(' ')[0] == 'SAMSUNG'):
				if ((len(pesquisado) - (len(aparelho)+11+5+8)) < 2):
					return True
				else:
					return False
			
			return True """
		# Fim das funções!

		print("OK1")	
		self.aparelho = completaEscolheCard(self.aparelho)
		try:	
			pesquisa = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/form/div[1]/div/input')
			
			print("OK2")
			pesquisa.send_keys(self.aparelho)
			print("OK3")
			pesquisa.send_keys(Keys.ENTER)
			print("OK4")
			print("Enter nas chaves",self.aparelho)
		
			preço = escolheCard(self.aparelho, driver)
			preço = precoFinal(preço)
		except Exception:
			preço = None


		if (preço is None) | (preço == ''):
			log = open('logs.txt', 'a')
			log.write('O preço do aparelho '+self.aparelho+' não foi encontrado no site: '+link_preço+'\n')
			log.close

		driver.close()
		return preço
