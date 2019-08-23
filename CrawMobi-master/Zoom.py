import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

class zoom:
	
	"""docstring for zoom"""
	
	def __init__(self, aparelho):
		super(zoom, self).__init__()
		self.aparelho = aparelho

	def preçoZoom(self):

		link_preço = 'https://www.zoom.com.br/celular' #site alternativo para aquisição dos preços em reais
		
		# Abrindo o navegador para realização da pesquisa do smartphone
		driver = webdriver.Chrome('/home/wandella/Documentos/CrawMobi-master/chromedriver')
		driver.get(link_preço)

		#Funções utilizadas na execução

		def precoFinal(preço): # Faz as alterações exatas no preço em Real
			preço = preço.split(' ')[1]
			preço = preço.replace('.','')
			preço = preço.replace(',','.')
			preço = float(preço)
			return preço

		# As funções a seguir escolhem o modal correto dentro do site Zoom a partir do nome do aparelho

		def escolheCard(aparelho, driver): # Comparação do nome para escolha correta, do card, no site Zoom
			pesquisado1 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]/h2/a').text
			print("Zoom Pesquisado 1",pesquisado1)

			if completaEscolheCard(aparelho, pesquisado1.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]/h2/a').click()
				print("Zoom 1")
			else:
				pesquisado2 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]/h2/a').text
				print("Zoom Pesquisado 2",pesquisado2)
			
			if completaEscolheCard(aparelho, pesquisado2.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]/h2/a').click()
				print("Zoom 2")
			else:
				pesquisado3 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[2]/h2/a').text
				print("Zoom Pesquisado 3",pesquisado3)
				
			if completaEscolheCard(aparelho, pesquisado3.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[2]/h2/a').click()
				print("Zoom 3")
			else:
				pesquisado4 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[4]/div[2]/h2/a').text
				
			if completaEscolheCard(aparelho, pesquisado4.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[4]/div[2]/h2/a').click()
				print("Zoom 4")
			else:
				pesquisado5 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[5]/div[2]/h2/a').text
				
			if completaEscolheCard(aparelho, pesquisado5.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[5]/div[2]/h2/a').click()
			else:
				pesquisado6 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[6]/div[2]/h2/a').text

			if completaEscolheCard(aparelho, pesquisado6.upper()):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[6]/div[2]/h2/a').click()

			if (pesquisado1.count(aparelho) == 1):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]/h2/a').click()
			if (pesquisado2.count(aparelho) == 1):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]/h2/a').click()
			if (pesquisado3.count(aparelho) == 1):
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[3]/div[2]/h2/a').click()


		# Função que complementa a função escolheCard(), vendo de qual marca é o aparelho para comparação
		def completaEscolheCard(aparelho, pesquisado):
			if (aparelho.split(' ')[0] == 'APPLE'):
				print("To no apple")
				if ((len(pesquisado) - (len(aparelho)+11+5)) < 2):
					return True
				else:
					return False
			
			if (aparelho.split(' ')[0] == 'MOTOROLA'):
				print("To no motorola")
				if ((len(pesquisado) - (len(aparelho)+11+5+7+2)) < 2):
					return True
				else:
					return False
			
			if (aparelho.split(' ')[0] == 'SAMSUNG'):
				if ((len(pesquisado) - (len(aparelho)+11+5+8)) < 2):
					return True
				else:
					return False
			
			return True
		# Fim das funções!
		
		try:
			if ((self.aparelho.split(' ')[0] == 'LENOVO') & (self.aparelho.split(' ')[1] == 'MOTO')): # Caso especial para os aprelhos da antiga motorola que estão como lenovo no kimovil mas como motorola no zoom
				self.aparelho = self.aparelho.replace('LENOVO MOTO ', '')
				self.aparelho = 'MOTOROLA MOTO '+aparelho[0]+' '+aparelho

			if (self.aparelho == 'XIAOMI POCOPHONE F1'): # Condição especial para o pocophone f1
				self.aparelho = self.aparelho.replace('XIAOMI ','')
			
			pesquisa = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/form/div[1]/div/input')
			pesquisa.send_keys(self.aparelho)
			pesquisa.send_keys(Keys.ENTER)
			
			try:
				#preço = driver.find_element_by_xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/div/div[2]/p/span[2]/a').text
				preço = driver.find_element_by_xpath('//*[@id="productInfo"]/div/div[2]/p/span[2]/a/strong').text
				print("Preço Zoom",preço)
				preço = precoFinal(preço)
			except Exception:
				try:
					escolheCard(self.aparelho, driver)
					#driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[1]').click()
					preço = driver.find_element_by_xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/div/div[2]/p/span[2]/a').text
					preço = precoFinal(preço)
				except Exception:
					try:
						driver.find_element_by_xpath('//*[@id="mobile-container"]/div[1]/section/div[2]/div/div[1]/ul/li[1]/div/div[2]/p[1]/a').click()
						escolheCard(self.aparelho, driver)
						#driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[1]').click()
						preço = driver.find_element_by_xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/div/div[2]/p/span[2]/a').text
						preço = precoFinal(preço)
					except Exception:
						try:
							preço = driver.find_element_by_xpath('//*[@id="mobile-container"]/div[1]/section/header/div/div[2]/div[1]/div[2]/div/div[2]/p/span[2]/a').text
							preço = precoFinal(preço)
						except Exception:
							preço = ''
		except Exception:
			preço = ''
		
		if (preço is None) | (preço == ''):
			log = open('logs.txt', 'a')
			log.write('O preço do aparelho '+self.aparelho+' não foi encontrado no site: '+link_preço+'\n')
			log.close()  
		
		driver.close()
		
		return preço