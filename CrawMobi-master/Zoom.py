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
		print("Entrando no site")
		link_preço = 'https://www.zoom.com.br/celular' #site alternativo para aquisição dos preços em reais
		
		# Abrindo o navegador para realização da pesquisa do smartphone
		driver = webdriver.Chrome('/home/wandella/Documentos/CrawMobi/CrawMobi-master/chromedriver')
		driver.get(link_preço)
		

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
			if pesquisado1.find(aparelho)>-1:
				print("zoom Achei 1",pesquisado1)
				driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[2]').click()
				print("Preço")
				#Preço = driver.find_element_by_xpath('//*[@id="productInfo"]/div/div[2]/p/span[2]/a/strong').text #Kimovil
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[1]/div[3]/span[2]/a[1]').text #Kimovil
				print(Preço)
				return Preço

			else:
				pesquisado2 = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]/h2/a').text
				pesquisado2 = pesquisado2.upper()
				print("zomm aparelho",pesquisado2)
			if pesquisado2.find(aparelho)>-1:
				print("zoom Achei 2",pesquisado2)
				#driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[2]').click()
				print("Preço")
				#Preço = driver.find_element_by_xpath('//*[@id="productInfo"]/div/div[2]/p/span[2]/a/strong').text #Kimovil
				Preço = driver.find_element_by_xpath('//*[@id="storeFrontList"]/li[2]/div[3]/span[2]/a[1]').text #Kimovil
				print(Preço)
				return Preço
				
			
			
		# Função que complementa a função escolheCard(), vendo de qual marca é o aparelho para comparação
		def completaEscolheCard(aparelho, pesquisado):
			print("Zoom completando card")
			if (aparelho.split(' ')[0] == 'APPLE'):
				if ((len(pesquisado) - (len(aparelho)+11+5)) < 2):
					return True
				else:
					return False
			
			if (aparelho.split(' ')[0] == 'MOTOROLA'):
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
					
		print("Cheguei até aqui no try")
		try:
			print("Vou pesquisar o celular")	
			pesquisa = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/form/div[1]/div/input')
			pesquisa.send_keys(self.aparelho)
			pesquisa.send_keys(Keys.ENTER)
			print("Indo escolher o card",self.aparelho)
			preço = escolheCard(self.aparelho, driver)
			print("Terminei o card")
			preço = precoFinal(preço)
			print("Confere retorno do preço->",preço)
		except Exception:
			preço = ''

		if (preço is None) | (preço == ''):
			log = open('logs.txt', 'a')
			log.write('O preço do aparelho '+self.aparelho+' não foi encontrado no site: '+link_preço+'\n')
			log.close

		driver.close()
		return preço
