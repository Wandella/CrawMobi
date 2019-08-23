import pandas as pd
import numpy
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re

import Zoom
import Celular

class kimovil:

	"""docstring for kimovil"""

	def __init__(self, aparelho):
		super(kimovil, self).__init__()
		self.aparelho = aparelho

	def executa(self):
		
		# Site que iremos procurar os smartphones
		link = 'https://www.kimovil.com/pt/comparar-celulares'

		# Navegadores abertos para pesquisa do elementos
		driver = webdriver.Chrome('/home/wandella/Documentos/CrawMobi-master/chromedriver')
		driver.get(link)
		
		celular = Celular.celular()
		
		# Funções utilizadas na execução
		''' Função para procurar o aparelho correto, dentro dos disponíveis após pesquisa, no site Kimovil.
		Depois da pesquisa são dados vários cards contendo celulares com nomes parecidos. Todo trabalho abaixo consiste em 
		verificar nos 15 primeiros cards se possuem o nome idêntico ao pesquisado no site kimovil. Caso não ocorra a 
		incidência, o aparelho é dado como não encontrado '''
		def escolhe(aparelho, driver, celular, link):
			#print("Aquiiiii")
			# Wandella : -Não entendi este método
			if (driver.find_element_by_xpath('//*[@id="results"]/div[3]/h3').text): # Caso em que o nome procurado não é encontrado no site
				#print("Aquiiiii")
				log = open('logs.txt', 'a')
				log.write('O Aparelho '+aparelho+' não foi encontrado, com esse nome, no site '+link+'.\n\n')
				log.close()
				return celular

			#print("Escolhendo card kimovil")
			#Olha o primeiro card para verificar se é o celular que procuramos
			principal_cel1 = driver.find_element_by_xpath('//*[@id="results-list"]/li[1]/div/a[2]/div[2]/div[1]').text
			principal_cel1 = principal_cel1.upper()
			#print("K aparelho",aparelho)
			#print("K ",principal_cel1)
			#Se for o celular encontrado, esta condição permite o clique sobre o card
			if aparelho == principal_cel1:
				#print("K Achei 1")
				driver.find_element_by_xpath('//*[@id="results-list"]/li[1]/div/a[2]').click()
				#print("K cliquei 1")
				getValueKimovil(aparelho, driver, celular) 
				return celular
			else:
				principal_cel2 = driver.find_element_by_xpath('//*[@id="results-list"]/li[2]/div/a[2]/div[2]/div[1]').text
				principal_cel2 = principal_cel2.upper()
				#print("K aparelho",aparelho)
				#print("K ",principal_cel2)
			if aparelho == principal_cel2:
				#print("K Achei 2")
				driver.find_element_by_xpath('//*[@id="results-list"]/li[2]/div/a[2]').click()
				#print("K cliquei 2")
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				principal_cel3 = driver.find_element_by_xpath('//*[@id="results-list"]/li[3]/div/a[2]/div[2]/div[1]').text
				principal_cel3 = principal_cel3.upper()
				#print("K aparelho",aparelho)
				#print("K ",principal_cel3)
			if aparelho == principal_cel3:
				#print("K Achei 3")
				driver.find_element_by_xpath('//*[@id="results-list"]/li[3]/div/a[2]').click()
				#print("K cliquei 3")
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				print("No 4")
				principal_cel4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]').text
				principal_cel4 = principal_cel4.upper()
			if aparelho == principal_cel4:        
				driver.find_element_by_xpath('//*[@id="results-list"]/li[4]/div/a[2]').click()        
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:        
				principal_cel5 = driver.find_element_by_xpath('//*[@id="results-list"]/li[5]/div/a[2]/div[2]/div[1]').text
				principal_cel5 = principal_cel5.upper()
				print("Cheguei até aqui",principal_cel5)
			if aparelho == principal_cel5:
				print("Foi",principal_cel5)
				driver.find_element_by_xpath('//*[@id="results-list"]/li[5]/div/a[2]').click()
				print("Cliquei 5")
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel6 = driver.find_element_by_xpath('//*[@id="results-list"]/li[6]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel6.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[6]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel7 = driver.find_element_by_xpath('//*[@id="results-list"]/li[7]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel7.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[7]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel8 = driver.find_element_by_xpath('//*[@id="results-list"]/li[8]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel8.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[8]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel9 = driver.find_element_by_xpath('//*[@id="results-list"]/li[9]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel9.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[9]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel10 = driver.find_element_by_xpath('//*[@id="results-list"]/li[10]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel10.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[10]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel11 = driver.find_element_by_xpath('//*[@id="results-list"]/li[11]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel11.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[11]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel12 = driver.find_element_by_xpath('//*[@id="results-list"]/li[12]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel12.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[12]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel13 = driver.find_element_by_xpath('//*[@id="results-list"]/li[13]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel13.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[13]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel14 = driver.find_element_by_xpath('//*[@id="results-list"]/li[14]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel14.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[14]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular
			else:
				principal_cel15 = driver.find_element_by_xpath('//*[@id="results-list"]/li[15]/div[2]/a[2]/div[2]/div[1]/span[1]').text

			if aparelho == principal_cel15.upper():
				smartphone = driver.find_element_by_xpath('//*[@id="results-list"]/li[15]/div[2]/a[2]/div[2]/div[1]/span[1]').click()
				getValueKimovil(aparelho, driver, celular)
				return celular

		# Função para atribuição dos valores ao objeto celular
		def getValueKimovil(aparelho, driver, celular):
			try:
				#print("Marca")
				Marca = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[1]/div/dl[1]/dd[1]').text #Kimovil
				#print(Marca)
				temp_marca = Marca.split("\n")
				#print(temp_marca[0])
				celular.setMarca(temp_marca[0])
			except Exception:
				celular.setMarca('')

			try:
				
				Modelo = driver.find_element_by_xpath('//*[@id="sec-start"]').text #Kimovil
				
				temp_modelo = Modelo.split("\n")
				
				celular.setModelo(temp_modelo[1])
			except Exception:
				celular.setModelo('')

			try:
				Capacidade_Bateria = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[7]/div/dl/dd[1]').text #Kimovil
				
				celular.setBateria(Capacidade_Bateria.split(" ")[0])
			except Exception:
				celular.setBateria('')

			try:
				Memoria_Ram = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[3]/div[1]/dl[3]/dd[1]').text #Kimovil
				Memoria_Ram = Memoria_Ram.split(" ")[0]
				
				if (float(Memoria_Ram) > 100): #Comparando como float
					nova_Memoria_Ram = ('0' + '.' + Memoria_Ram) # Adicionando o "0." para transformar de MB para GB
				else:
					nova_Memoria_Ram = Memoria_Ram

				celular.setRam(nova_Memoria_Ram)
			except Exception:
				celular.setRam('')

			try:
				Memoria_Armazenamento = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[3]/div[1]/dl[5]/dd[1]').text #Kimovil
				temp_Armazenamento = re.findall(r'\d+', Memoria_Armazenamento)
				
				celular.setArmazenamento(temp_Armazenamento[0])
			except Exception:                            
				celular.setArmazenamento('')

			try:                            
				Bluetooth = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[6]/div[3]/dl[4]/dd[1]').text #Kimovil
				temp_Bluetooth = re.findall(r'(\d+\.\d+)', Bluetooth)

				celular.setBluetooth(temp_Bluetooth[0])
			except Exception:
				celular.setBluetooth('')

			try:
				# função para encontrar nfc
				NFC = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[6]/div[3]/dl[8]/dd[1]').text #Kimovil        
				
				if (NFC == 'Sim' or NFC == 'sim' or NFC == 'SIM'):
					
					celular.setNfc('SIM')
				else:
					
					celular.setNfc('NAO')
			except Exception:
				celular.setNfc('')

			try:
				Dual_chip = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[6]/div[3]/dl[2]/dd').text #Kimovil

				if (Dual_chip.split(' ')[0] == 'Single'):
					celular.setDualChip('NAO')
				else:
					celular.setDualChip('SIM')
			except Exception:
				celular.setDualChip('')

			try:
				Lte = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[6]/div[3]/dl[1]/dt[1]').text #Kimovil        

				if (Lte.split(' ')[0] == '4G'):
					celular.setLte('SIM')
				else:
					celular.setLte('NAO')

			except Exception:
				celular.setLte('')

			try:
				Resoluçao_camera = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[4]/div/div[1]/div[1]/dl/dd[2]').text #Kimovil
				#print("Resoliucao cam",Resoluçao_camera.split(" ")[0])
				celular.setResolucaoCam(Resoluçao_camera.split(" ")[0])
			except Exception:
				celular.setResolucaoCam('')

			try:
				Peso = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[2]/div/dl[1]/dd[2]').text #Kimovil

				celular.setPeso(Peso.split(' ')[0])
			except Exception:
				celular.setPeso('')

			try:
				Dimensao = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[2]/div/dl[1]/dd[1]').text #Kimovil
				numero = re.findall(r'\d+.\d+', Dimensao)

				celular.setDimensoes('{0}x{1}x{2}'.format(numero[0],numero[1],numero[2]))
			except Exception:
				celular.setDimensoes('')

			try:
				Tamanho_tela = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[2]/div/dl[2]/dd[1]').text #Kimovil

				celular.setTela(Tamanho_tela.split('"')[0])
			except Exception:
				celular.setTela('')

			try:
				#print("Kimovil entrei no SO")
				SO = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[8]/div/dl/dd').text #Kimovil
				#print("SO",SO)
				celular.setSo(SO.split(' ')[0])
			except Exception:
				celular.setSo('')

			#Arrumar depois, pois está uma bagunça
			""" try:
				#Versao_SO = driver.find_element_by_xpath('//*[@id="software"]/div/div[1]/div[2]/dl/dd/p/small').text #Kimovil
				Versao_SO = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[8]/div/dl/dd').text #Kimovil
				temp = Versao_SO.split('')[1]
				print("Versao SO", temp.split('\n')[0])	
				celular.setVersaoSo(temp.split('\n')[0])
			except Exception:
				celular.setVersaoSo('')
 """
			try:
				Processamento = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[3]/div[1]/dl[1]/dd[4]').text
				proc_temp = Processamento.split(" ")[0]
				if proc_temp.find('.') > -1:
					celular.setProcessamento(proc_temp)
				else:
					proc_temp = proc_temp/1000
					celular.setProcessamento(proc_temp)
			except Exception:
				celular.setProcessamento('')

			try:
				celular.setFonte(link) #Geral
			except Exception:
				celular.setFonte('')

			try:
				Data_atualizacao = time.strftime('%m/%Y') #Geral

				celular.setData(Data_atualizacao)
			except Exception:
				celular.setData('')

			try:
				Ano_lancamento = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[5]/section[1]/div/dl[2]/dd[1]').text #Kimovil
						
				celular.setDataLancamento(padraoData(Ano_lancamento.split(',')[0]))
			except Exception:
				celular.setDataLancamento('')

			try:
				Avaliacao_site = driver.find_element_by_xpath('//*[@id="sec-datasheet"]/li[1]/div/div[1]/div[2]/span').text #Kimovil
				#print("AV Site",Avaliacao_site)
				if (Avaliacao_site == 'Não preço,\nnão Ki'):
					celular.setAvaliacaoSite('')

				celular.setAvaliacaoSite(Avaliacao_site)
			except Exception:
				celular.setAvaliacaoSite('')

			try:        
				Avaliacao_Usuario = driver.find_element_by_xpath('//*[@id="sec-datasheet"]/li[2]/div/a/div[2]/div').text #Kimovil
				#print("AV USU",Avaliacao_Usuario)
				celular.setAvaliacaoUsu(Avaliacao_Usuario)
			except Exception:
				celular.setAvaliacaoUsu('')

			return celular
			try:
				print("Antes do Preco kimovil")
				#driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[1]/div/button[1]/div[1]').click()
				preco = driver.find_element_by_xpath('//*[@id="margin"]/div[2]/div/div[1]/div/button[1]/div[2]').text #Kimovil
				print("Preco kimovil",preco)
				celular.setPreco(preco)
			except Exception:
				celular.setPreco('')

		def padraoData(data):
			mes = data.split(' ')
			if (mes[0] == 'Janeiro'):
				data = '01' + '/' + mes[1]
				return data
			if (mes[0] == 'Fevereiro'):
				data = '02' + '/' + mes[1]
				return data
			if (mes[0] == 'Março'):
				data = '03' + '/' + mes[1]
				return data
			if (mes[0] == 'Abril'):
				data = '04' + '/' + mes[1]
				return data
			if (mes[0] == 'Maio'):
				data = '05' + '/' + mes[1]
				return data
			if (mes[0] == 'Junho'):
				data = '06' + '/' + mes[1]
				return data
			if (mes[0] == 'Julho'):
				data = '07' + '/' + mes[1]
				return data
			if (mes[0] == 'Agosto'):
				data = '08' + '/' + mes[1]
				return data
			if (mes[0] == 'Setembro'):
				data = '09' + '/' + mes[1]
				return data
			if (mes[0] == 'Outubro'):
				data = '10' + '/' + mes[1]
				return data
			if (mes[0] == 'Novembro'):
				data = '11' + '/' + mes[1]
				return data
			if (mes[0] == 'Dezembro'):
				data = '12' + '/' + mes[1]
				return data
			return data

		# Fim das funções!
	
		pesquisa = driver.find_element_by_xpath('//*[@id="js_global-search-input"]')
		pesquisa.send_keys(self.aparelho)
		pesquisa.send_keys(Keys.ENTER)
		escolhe(self.aparelho, driver, celular, link)

		preço = Zoom.zoom(self.aparelho)

		celular.setPreco(preço.preçoZoom())

		driver.close()

		return celular