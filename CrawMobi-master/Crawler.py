import pandas as pd
import numpy
import csv
from zipfile import *
import xlsxwriter
import xlwt
import xlrd
import Celular
import Kimovil
import PhoneArena
import Comparador

class crawler:
	"""docstring for crawler"""
    
	def __init__(self):
		super(crawler, self).__init__()

	def menu(self):
		
		cel1 = Celular.celular()
		cel2 = Celular.celular()
		compara = Comparador.comparador()

		# Criando arquivo xls para escrita dos dados dos handsets
		workbook = xlsxwriter.Workbook('Dados_Smartphones.xls')
		worksheet = workbook.add_worksheet()

		# Criação dos metadados da tabela
		worksheet.write(0, 0, 'Marca')
		worksheet.write(0, 1, 'Modelo')
		worksheet.write(0, 2, 'Capacidade da Bateria (mAh)')
		worksheet.write(0, 3, 'Memória RAM (GB)')        
		worksheet.write(0, 4, 'Memória de Armazenamento (GB)')   
		worksheet.write(0, 5, 'Bluetooth')        
		worksheet.write(0, 6, 'NFC')        
		worksheet.write(0, 7, 'Dual Chip')
		worksheet.write(0, 8, 'LTE (4G)')        
		worksheet.write(0, 9, 'Resolução da Câmera (Mpx)')
		worksheet.write(0, 10, 'Peso (g)')        
		worksheet.write(0, 11, 'Dimensões')        
		worksheet.write(0, 12, 'Tamanho da Tela (")')        
		worksheet.write(0, 13, 'Sistema Operacional')        
		worksheet.write(0, 14, 'Versão SO')        
		worksheet.write(0, 15, 'Processamento (GHz)')        
		worksheet.write(0, 16, 'Link fonte')        
		worksheet.write(0, 17, 'Data de atualização')        
		worksheet.write(0, 18, 'Ano do lançamento')        
		worksheet.write(0, 19, 'Preço (R$)')        
		worksheet.write(0, 20, 'Avaliação do Site')        
		worksheet.write(0, 21, 'Avaliação dos Usuários')

		# Criação do arquivo contento os logs da aplicação
		log = open('logs.txt', 'w')
		log.write('Smartphones Description - Getting Database\n\n')
		log.write('Execution logs:\n\n')
		log.close()

		book = xlrd.open_workbook("ListaSmartphones.xls")
		sh = book.sheet_by_index(0)
		lista = []

		for rx in range(sh.nrows):
			lista.append(sh.row(rx))
		else:
			for linha, value in enumerate(lista):
				print(linha, value)

				try:
					# Pegando o conteúdo da lista de smartphones para pesquisa no site
					aparelho = str(lista[linha + 1]).split("'")[1].upper()
					print("Foi a vez do aparelho ",aparelho)
					kim = Kimovil.kimovil(aparelho)
					pha = PhoneArena.phoneArena(aparelho)
					cel1 = kim.executa()
					print("Kimovil executou")
					cel2 = pha.executa()
					print("Phonearena executou")
					compara.armazena(cel1, cel2, linha, worksheet)
					print("Fim")
				except Exception:
					print("NOT FOUND Crawler")

		log = open('logs.txt', 'a')
		log.write('A maioria dos dados escolhidos foram do site Kimovil por possuir uma base de dados mais extensa.\n\n')
		log.close()

		csvfile = "handsets.csv"
		f = open(csvfile, 'wb')  # Abre o arquivo para escrita apagando o conteúdo existente
		csv = pd.read_excel('Dados_Smartphones.xls')
		print(csv)
		csv.to_csv('handsets.csv', index=False)

		# Código para criação do arquivo zip
		with ZipFile('gettingDatabase.zip', 'w') as myzip:
			myzip.write('handsets.csv')
			myzip.write('logs.txt')