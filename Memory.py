from Consts import Consts
from SemanticVisitor import TNumber
from Error import Error
####################################### Tabela de simbolos (Symbol Table) #######################################
class SymbolTable:
	def __init__(self):
		self.symbols = {}
	def get(self, name):
		value = self.symbols.get(name, None)
		return value
	def set(self, name, value):
		self.symbols[name] = value
	def remove(self, name):
		del self.symbols[name]
####################################### Gerente de Memoria #######################################
class MemoryManager:
	singleton = None
	def __init__(self):
		if MemoryManager.singleton!=None: 
			raise Exception(f"{Error.singletonMsg(self)}.instanceOfMemoryManager(resetErrors=True)'!")
		self.value = None
		self.error = None
		MemoryManager.singleton = self
		self.configSymbolTable()

	def configSymbolTable(self):# Criando a tabela de simbolos:
		self.symbolTable = SymbolTable()
		self.symbolTable.set(Consts.NULL, TNumber(0)) # Chave 'null', Valor Objeto TNumber como valor zero

	def registry(self, rtr):
		if rtr.error: self.error = rtr.error
		return rtr.value
	def success(self, value):
		self.value = value
		return self
	def fail(self, error):
		self.error = error
		return self
	
	@staticmethod	
	def resetSingletonError():
		MemoryManager.singleton.error = None
		return MemoryManager.singleton
	
	@staticmethod
	def instanceOfMemoryManager(resetErrors=True):
		if MemoryManager.singleton==None:
			MemoryManager.singleton = MemoryManager()
		return MemoryManager.resetSingletonError() if resetErrors else MemoryManager.singleton
