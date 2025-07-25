#import abc
from Error import Error
from Consts import Consts

class TValue(): 
	def __init__(self) -> None:
		self.value = None

	def setMemory(self, memory=None): return self.exceptionError(f"The 'setMemory({memory})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def add(self, other): return self.exceptionError(f"The 'add({self}{Consts.PLUS}{other})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def sub(self, other): return self.exceptionError(f"The 'sub({self}{Consts.MINUS}{other})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def mult(self, other): return self.exceptionError(f"The 'mult({self}{Consts.MUL}{other})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def div(self, other): return self.exceptionError(f"The 'div({self}{Consts.DIV}{other})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def pow(self, other): return self.exceptionError(f"The 'pow({self}{Consts.POW}{other})' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	def copy(self): return self.exceptionError(f"The 'copy()' method not suported on the {Error.classNameOf(self)} class!") #raise NotImplementedError
	
	def exceptionError(self, error_msn: str): return None, Error(f"{Error.runTimeError}: {error_msn}")

	def __eq__(self, value: object) -> bool:
		if isinstance(value, TValue):
			return self.value == value.value
		return False
	
	def __hash__(self) -> int:
		return hash(self.value)

class TNumber(TValue):
	def __init__(self, value):
		self.value = value
		self.setMemory()
	def setMemory(self, memory=None):
		self.memory = memory
		return self
	def add(self, other):
		if isinstance(other, TNumber):
			return TNumber(self.value + other.value).setMemory(self.memory), None
		return super().add(other)
	def sub(self, other):
		if isinstance(other, TNumber):
			return TNumber(self.value - other.value).setMemory(self.memory), None
		return super().sub(other)
	def mult(self, other):
		if isinstance(other, TNumber):
			return TNumber(self.value * other.value).setMemory(self.memory), None
		return super().mult(other)
	def div(self, other):
		if isinstance(other, TNumber):
			if other.value == 0:
				return self.exceptionError("Divisao por zero")
			return TNumber(self.value / other.value).setMemory(self.memory), None
		return super().div(other)
	def pow(self, other):
		if isinstance(other, TNumber):
			return TNumber(self.value ** other.value).setMemory(self.memory), None
		return super().pow(other)
	def copy(self):
		copy = TNumber(self.value)
		copy.setMemory(self.memory)
		return copy	
	def __repr__(self):
		return str(self.value)
class TString(TValue):
	def __init__(self, value):
		self.value = value
		self.setMemory()
	def setMemory(self, memory=None):
		self.memory = memory
		return self
	def add(self, other):
		if isinstance(other, TString):
			return TString(self.value + other.value).setMemory(self.memory), None
		return super().add(other)
	def copy(self):
		copy = TString(self.value)
		copy.setMemory(self.memory)
		return copy		
	def __repr__(self):
		return f'"{str(self.value)}"'
##############################
class TList(TValue):
	def __init__(self, value):
		self.value = value
		self.setMemory()
	def setMemory(self, memory=None):
		self.memory = memory
		return self
	def add(self, other):
		if isinstance(other, TList):
			return TList(self.value + other.value).setMemory(self.memory), None
		return super().add(other)
	def copy(self):
		copy = TList(self.value)
		copy.setMemory(self.memory)
		return copy	
	
	def __repr__(self):
		return f"{str(self.value)}"
##############################
class TTupla(TValue):
    def __init__(self, value):
        self.value = tuple(value) if isinstance(value, list) else value
        self.setMemory()
    
    def setMemory(self, memory=None):
        self.memory = memory
        return self
    
    def add(self, other):
        if isinstance(other, TTupla):
            return TTupla(self.value + other.value).setMemory(self.memory), None
        return super().add(other)
    
    def copy(self):
        copy = TTupla(self.value)
        copy.setMemory(self.memory)
        return copy
    
    def __repr__(self):
        if len(self.value) == 0:
            return "()"
        elif len(self.value) == 1:
            return f"({self.value[0]},)"
        else:
            elementos_str = ", ".join(str(elem) for elem in self.value)
            return f"({elementos_str})"
		
# ======================================
# ITEM 2: TIPO CRIATIVO - DICIONÁRIO/MAPA
# ======================================

# MODIFICAÇÕES NO CONSTS.PY (adicionar):
# LBRACE = '{'
# RBRACE = '}'
# COLON = ':'

# MODIFICAÇÕES NO LEXER.PY:
# elif self.current == Consts.LBRACE:
#     tokens.append(Token(Consts.LBRACE))
#     self.__advance()
# elif self.current == Consts.RBRACE:
#     tokens.append(Token(Consts.RBRACE))
#     self.__advance()
# elif self.current == Consts.COLON:
#     tokens.append(Token(Consts.COLON))
#     self.__advance()

class TDict(TValue):
    def __init__(self, value):
        self.value = value if isinstance(value, dict) else {}
        self.setMemory()
    
    def setMemory(self, memory=None):
        self.memory = memory
        return self
    
    def add(self, other):
        if isinstance(other, TDict):
            novo_dict = self.value.copy()
            novo_dict.update(other.value)
            return TDict(novo_dict).setMemory(self.memory), None
        return super().add(other)
    
    def get_item(self, chave):
        """Método para acessar elementos do dicionário"""
        if chave in self.value:
            return self.value[chave].copy(), None
        return None, Error(f"{Error.runTimeError}: Chave '{chave}' não encontrada no dicionário")
    
    def set_item(self, chave, valor):
        """Método para definir elementos do dicionário"""
        if not isinstance(chave, (TNumber, TString)):
            return None, Error(f"{Error.runTimeError}: Chave do dicionário deve ser um número ou string")
        self.value[chave] = valor
        return valor, None
    
    def copy(self):
        novo_dict = {}
        for k, v in self.value.items():
            novo_dict[k] = v.copy()
        copy = TDict(novo_dict)
        copy.setMemory(self.memory)
        return copy
    
    def keys(self):
        """Retorna uma lista com todas as chaves"""
        return TList([chave.copy() for chave in self.value.keys()]), None
    
    def values(self):
        """Retorna uma lista com todos os valores"""
        return TList([valor.copy() for valor in self.value.values()]), None
    
    def __repr__(self):
        if not self.value:
            return "{}"
        
        items = []
        for chave, valor in self.value.items():
            items.append(f"{chave}: {valor}")
        
        return "{" + ", ".join(items) + "}"
