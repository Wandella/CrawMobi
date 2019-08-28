import xlsxwriter
import xlwt
import xlrd

class comparador:
	
	"""docstring for comparador"""
	
	def __init__(self):
		super(comparador, self).__init__()

	def armazena(self, cel1, cel2, linha, worksheet):
		# Função para escrita no dataFrame
		
		worksheet.write(linha + 1, 0, cel1.getMarca())
		#print("Marca do cel 1",cel1.getMarca())
		#print("Marca do cel 2",cel2.getMarca())
		if (cel2.getMarca()):
			#print("Marca Phonearena")
			worksheet.write(linha + 1, 2, cel2.getMarca())

			""" log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Bateria no Kimovil: '+cel1.getMarca+'. Bateria no phoneArena: '+cel2.getBateria()+'.\n')
			log.write('O valor para bateria escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close() """
		else:
			#print("Marca kimovil")
			worksheet.write(linha + 1, 2, cel1.getMarca())

		worksheet.write(linha + 1, 1, cel1.getModelo())
		#print("Moodelo do cel 1",cel1.getModelo())
		#print("Modelo do cel 2",cel2.getModelo())
		if (cel2.getModelo()):
			#print("Modelo Phonearena")
			worksheet.write(linha + 1, 2, cel2.getModelo())

			""" log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Bateria no Kimovil: '+cel1.getMarca+'. Bateria no phoneArena: '+cel2.getBateria()+'.\n')
			log.write('O valor para bateria escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close() """
		else:
			#print("Modelo kimovil")
			worksheet.write(linha + 1, 2, cel1.getModelo())

		
		if (cel1.getBateria() != cel2.getBateria()):
			#print("Case 1 bateria")
			worksheet.write(linha + 1, 2, cel1.getBateria())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Bateria no Kimovil: '+cel1.getBateria()+'. Bateria no phoneArena: '+cel2.getBateria()+'.\n')
			log.write('O valor para bateria escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			#print("Bateria foi")
			worksheet.write(linha + 1, 2, cel1.getBateria())


		if (cel1.getRam() != cel2.getRam()):

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Memória Ram no Kimovil: '+cel1.getRam()+'. Memória Ram no phoneArena: '+cel2.getRam()+'.\n')

			if (cel1.getRam() < cel2.getRam()):
				worksheet.write(linha + 1, 3, cel1.getRam())

				log.write('O valor para Memória Ram escolhido foi do site Kimovil por ser o menor entre os dois.\n\n')
			else:
				worksheet.write(linha + 1, 3, cel2.getRam())

				log.write('O valor para Memória Ram escolhido foi do site PhoneArena por ser o menor entre os dois.\n\n')
				
			log.close()
		else:
			worksheet.write(linha + 1, 3, cel1.getRam())

		if (cel1.getArmazenamento() != cel2.getArmazenamento()):

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Memória de Armazenamento no Kimovil: '+cel1.getArmazenamento()+'. Memória de Armazenamento no phoneArena: '+cel2.getArmazenamento()+'.\n')

			if (cel1.getArmazenamento() < cel2.getArmazenamento()):
				worksheet.write(linha + 1, 4, cel1.getArmazenamento())

				log.write('O valor para Memória de Armazenamento escolhido foi do site Kimovil por ser o menor entre os dois.\n\n')
			else:
				worksheet.write(linha + 1, 4, cel2.getArmazenamento())

				log.write('O valor para Memória de Armazenamento escolhido foi do site PhoneArena por ser o menor entre os dois.\n\n')
				
			log.close()
		else:
			worksheet.write(linha + 1, 4, cel1.getArmazenamento())

		if (cel1.getBluetooth() != cel2.getBluetooth()):
			
			worksheet.write(linha + 1, 5, cel1.getBluetooth())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Bluetooth no Kimovil: '+cel1.getBluetooth()+'. Bluetooth no phoneArena: '+cel2.getBluetooth()+'.\n')
			log.write('O valor para Bluetooth escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 5, cel1.getBluetooth())

		if (cel1.getNfc() != cel2.getNfc()):
			
			worksheet.write(linha + 1, 6, cel1.getNfc())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. NFC no Kimovil: '+cel1.getNfc()+'. NFC no phoneArena: '+cel2.getNfc()+'.\n')
			log.write('O valor para NFC escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 6, cel1.getNfc())

		if (cel1.getDualChip() != cel2.getDualChip()):
			
			worksheet.write(linha + 1, 7, cel1.getDualChip())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Dual Chip no Kimovil: '+cel1.getDualChip()+'. Dual Chip no phoneArena: '+cel2.getDualChip()+'.\n')
			log.write('O valor para Dual Chip escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 7, cel1.getDualChip())

		if (cel1.getLte() != cel2.getLte()):
			
			worksheet.write(linha + 1, 8, cel1.getLte())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. LTE(4G) no Kimovil: '+cel1.getLte()+'. LTE(4G) no phoneArena: '+cel2.getLte()+'.\n')
			log.write('O valor para LTE(4G) escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 8, cel1.getLte())

		if (cel1.getResolucaoCam() != cel2.getResolucaoCam()):
			
			worksheet.write(linha + 1, 9, cel1.getResolucaoCam())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Resolução da Câmera no Kimovil: '+cel1.getResolucaoCam()+'. Resolução da Câmera no phoneArena: '+cel2.getResolucaoCam()+'.\n')
			log.write('O valor para a Resolução da Câmera escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 9, cel1.getResolucaoCam())

		if (cel1.getPeso() != cel2.getPeso()):
			
			worksheet.write(linha + 1, 10, cel1.getPeso())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Peso no Kimovil: '+cel1.getPeso()+'. Peso no phoneArena: '+cel2.getPeso()+'.\n')
			log.write('O valor para peso escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 10, cel1.getPeso())

		if (cel1.getDimensoes() != cel2.getDimensoes()):
			
			worksheet.write(linha + 1, 11, cel1.getDimensoes())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Dimensões no Kimovil: '+cel1.getDimensoes()+'. Dimensões no phoneArena: '+cel2.getDimensoes()+'.\n')
			log.write('O valor para as Dimensões escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 11, cel1.getDimensoes())

		if (cel1.getTela() != cel2.getTela()):
			
			worksheet.write(linha + 1, 12, cel1.getTela())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Tela no Kimovil: '+cel1.getTela()+'. Tela no phoneArena: '+cel2.getTela()+'.\n')
			log.write('O valor para o tamanho do Tela escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 12, cel1.getTela())

		if (cel1.getSo() != cel2.getSo()):
			
			worksheet.write(linha + 1, 13, cel1.getSo())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. SO no Kimovil: '+cel1.getSo()+'. SO no phoneArena: '+cel2.getSo()+'.\n')
			log.write('O valor para o SO escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			print("Para escrever",cel1.getSo())
			worksheet.write(linha + 1, 13, cel1.getSo())
			

		if (cel1.getVersaoSo() != ''):
			print("Cel 1 Versao SO",cel1.getVersaoSo())
			worksheet.write(linha + 1, 14, cel1.getVersaoSo())
		elif (cel2.getVersaoSo() != ''):
			print("Cel 2 Versao SO",cel2.getVersaoSo())
			worksheet.write(linha + 1, 14, cel2.getVersaoSo())

		if (cel2.getVersaoSo() != ''):
			log = open('logs.txt', 'a')
			log.write('O valor para a Versão do SO escolhido foi do site PhoneArena por possuir essa informação mais confiável.\n\n')
			log.close()

		if (cel1.getProcessamento() != cel2.getProcessamento()):
			
			worksheet.write(linha + 1, 15, cel1.getProcessamento())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Processamento no Kimovil: '+cel1.getProcessamento()+'. Processamento no phoneArena: '+cel2.getProcessamento()+'.\n')
			log.write('O valor para o Processamento escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 15, cel1.getProcessamento())

		worksheet.write(linha + 1, 16, cel1.getFonte())
		worksheet.write(linha + 1, 17, cel1.getData())

		if (cel1.getDataLancamento() != cel2.getDataLancamento()):
			
			worksheet.write(linha + 1, 18, cel1.getDataLancamento())

			log = open('logs.txt', 'a')
			log.write('Houve divergência de valores no aparelho '+cel1.getModelo()+'. Data de lançamento no Kimovil: '+cel1.getDataLancamento()+'. Data de lançamento no phoneArena: '+cel2.getDataLancamento()+'.\n')
			log.write('O valor para a data de lançamento escolhido foi do site Kimovil por possuir uma base de dados mais confiável.\n\n')
			log.close()
		else:
			worksheet.write(linha + 1, 18, cel1.getDataLancamento())

		if cel1.getPreco() != None:
			print("Escrevendo Preço caso1", cel1.getPreco())
			worksheet.write(linha + 1, 19, cel1.getPreco())
		else:
			print("Escrevendo Preço caso3", cel1.getPreco())
			worksheet.write(linha + 1, 19, None)
		
		#Inserir avaliação do site
		avaliacao_site = cel1.getAvaliacaoSite()
		if avaliacao_site.isdigit() == False:
			worksheet.write(linha + 1, 20,avaliacao_site)
		else:
			worksheet.write(linha + 1, 20,None)
		
		#Inserir avaliação do usuario
		avaliacao_usuario = cel1.getAvaliacaoUsu()
		if avaliacao_usuario.isdigit() == False:
			worksheet.write(linha + 1, 21,avaliacao_usuario)
		else:
			worksheet.write(linha + 1, 21,None)