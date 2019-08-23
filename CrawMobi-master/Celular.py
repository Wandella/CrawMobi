class celular():
	"""docstring for celular"""

	marca = ''
	modelo = ''
	bateria = ''
	ram = ''
	armazenamento = ''
	bluetooth = ''
	nfc = ''
	dualChip = ''
	lte = ''
	resolucaoCam = ''
	peso = ''
	dimensoes = ''
	tela = ''
	so = ''
	versaoSo = ''
	processamento = ''
	fonte = ''
	data = ''
	dataLancamento = ''
	preco = ''
	avaliacaoSite = ''
	avaliacaoUsu = ''

	""" Construtor da classe celular """
	def __init__(self):
		super(celular, self).__init__()

	""" Métodos setters """
	def setMarca(self, marca):
		self.marca = marca

	def setModelo(self, modelo):
		self.modelo = modelo

	def setBateria(self, bateria):
		self.bateria = bateria

	def setRam(self, ram):
		self.ram = ram

	def setArmazenamento(self, armazenamento):
		self.armazenamento = armazenamento

	def setBluetooth(self, bluetooth):
		self.bluetooth = bluetooth

	def setNfc(self, nfc):
		self.nfc = nfc

	def setDualChip(self, dualChip):
		self.dualChip = dualChip

	def setLte(self, lte):
		self.lte = lte

	def setResolucaoCam(self, resolucaoCam):
		self.resolucaoCam = resolucaoCam

	def setPeso(self, peso):
		self.peso = peso

	def setDimensoes(self, dimensoes):
		self.dimensoes = dimensoes

	def setTela(self, tela):
		self.tela = tela

	def setSo(self, so):
		self.so = so

	def setVersaoSo(self, versaoSo):
		self.versaoSo = versaoSo

	def setProcessamento(self, processamento):
		self.processamento = processamento

	def setFonte(self, fonte):
		self.fonte = fonte

	def setData(self, data):
		self.data = data

	def setDataLancamento(self, dataLancamento):
		self.dataLancamento = dataLancamento

	def setPreco(self, preco):
		self.preco = preco

	def setAvaliacaoSite(self, avaliacaoSite):
		self.avaliacaoSite = avaliacaoSite

	def setAvaliacaoUsu(self, avaliacaoUsu):
		self.avaliacaoUsu = avaliacaoUsu


	""" Métodos getters """
	def getMarca(self):
		return self.marca

	def getModelo(self):
		return self.modelo

	def getBateria(self):
		return self.bateria

	def getRam(self):
		return self.ram

	def getArmazenamento(self):
		return self.armazenamento

	def getBluetooth(self):
		return self.bluetooth

	def getNfc(self):
		return self.nfc

	def getDualChip(self):
		return self.dualChip

	def getLte(self):
		return self.lte

	def getResolucaoCam(self):
		return self.resolucaoCam

	def getPeso(self):
		return self.peso

	def getDimensoes(self):
		return self.dimensoes

	def getTela(self):
		return self.tela

	def getSo(self):
		return self.so

	def getVersaoSo(self):
		return self.versaoSo

	def getProcessamento(self):
		return self.processamento

	def getFonte(self):
		return self.fonte

	def getData(self):
		return self.data

	def getDataLancamento(self):
		return self.dataLancamento

	def getPreco(self):
		return self.preco

	def getAvaliacaoSite(self):
		return self.avaliacaoSite

	def getAvaliacaoUsu(self):
		return self.avaliacaoUsu