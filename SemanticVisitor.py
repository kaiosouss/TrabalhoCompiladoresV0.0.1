from Error import Error
import abc
from TValue import *
from Consts import Consts
from Memory import MemoryManager
"""
# * Aqui são incluídos os NO's da AST (Abstract Syntax Tree).
# * Eles aceitam visitas de operadores de memoria, visando semantica e controle de tipos (para execucao ou compilacao).
# * Tipos: - criamos a classe TValue especializada em tratar tipos e valores.
#         - Partimos da ideia de que todo dado possui um tipo e valor.

"""
class Visitor(metaclass=abc.ABCMeta): # OBS: os parametros "operator" sao do tipo "MemoryManager", para "runtime" e acesso a memória/tabela de simbolos
	@abc.abstractmethod
	def visit(self, operator): operator.fail(Error(f"{Error.runTimeError}: Nenhum metodo visit para a classe '{Error.classNameOf(self)}' foi definido!"))

	def __repr__(self): (f"TODO: implements __repr__ of '{Error.classNameOf(self)}' class")
	
class NoTupla(Visitor):
    def __init__(self, elementos):
        self.elementos = elementos

    def visit(self, operator):
        tValue = []
        for elemento_node in self.elementos:
            tValue.append(operator.registry(elemento_node.visit(operator)))
            if operator.error: return operator
        
        return operator.success(TTupla(tValue).setMemory(operator))

    def __repr__(self):
        return f'({self.elementos})'
		
class NoNumber(Visitor):
	def __init__(self, tok):
		self.tok = tok

	def visit(self, operator):
		return operator.success(TNumber(self.tok.value).setMemory(operator))

	def __repr__(self):
		return f'{self.tok}'
	
class NoOpUnaria(Visitor):
	def __init__(self, opTok, node):
		self.opTok = opTok
		self.node = node

	def visit(self, operator):
		num = operator.registry(self.node.visit(operator))
		if operator.error: return operator
		error = None
		if self.opTok.type == Consts.MINUS:
			num, error = num.mult(TNumber(-1))
		if error:
			return operator.fail(error)
		else:
			return operator.success(num)

	def __repr__(self):
		return f'({self.opTok}, {self.node})'

class NoOpBinaria(Visitor):
	def __init__(self, leftNode, opTok, rightNode):
		self.noEsq = leftNode
		self.opTok = opTok
		self.noDir = rightNode
	
	def __repr__(self):
		return f'({self.noEsq}, {self.opTok}, {self.noDir})'
	
	@staticmethod
	def Perform(GVar1, ops, GVar2=None): # Grammar Var (GVar), Operator options (ops=+,- ou *, /)
		if GVar2==None: GVar2 = GVar1
		ast = GVar1.GetParserManager()
		op_bin_ou_esq = ast.registry(GVar1.Rule())
		if ast.error: return ast
		while GVar1.CurrentToken().type in ops:
			token_operador = GVar1.CurrentToken()
			GVar1.NextToken()
			lado_direito = ast.registry(GVar2.Rule())
			if ast.error: return ast
			op_bin_ou_esq = NoOpBinaria(op_bin_ou_esq, token_operador, lado_direito)
		return ast.success(op_bin_ou_esq)
	
	def visit(self, operator):
		esq = operator.registry(self.noEsq.visit(operator))
		if operator.error: return operator
		dir = operator.registry(self.noDir.visit(operator))
		if operator.error: return operator

		if self.opTok.type == Consts.PLUS:
			result, error = esq.add(dir)
		elif self.opTok.type == Consts.MINUS:
			result, error = esq.sub(dir)
		elif self.opTok.type == Consts.MUL:
			result, error = esq.mult(dir)
		elif self.opTok.type == Consts.DIV:
			result, error = esq.div(dir)
		elif self.opTok.type == Consts.POW:
			result, error = esq.pow(dir)

		if error:
			return operator.fail(error)
		else:
			return operator.success(result)
##############################
class NoVarAssign(Visitor):
	def __init__(self, varNameTok, valueNode):
		self.varNameTok = varNameTok
		self.valueNode = valueNode

	def visit(self, operator):
		varName = self.varNameTok.value
		value = operator.registry(self.valueNode.visit(operator))
		if operator.error: return operator

		operator.symbolTable.set(varName, value)
		return operator.success(value)

	def __repr__(self):
		return f'({self.varNameTok}, {self.valueNode})'
	
class NoVarAccess(Visitor):
	def __init__(self, varNameTok):
		self.varNameTok = varNameTok

	def visit(self, operator):
		varName = self.varNameTok.value
		value = operator.symbolTable.get(varName)

		if not value: return operator.fail(Error(f"{Error.runTimeError}: '{varName}' nao esta definido"))

		value = value.copy()
		return operator.success(value)

	def __repr__(self):
		return f'({self.varNameTok})'
class NoString(Visitor):
	def __init__(self, tok):
		self.tok = tok

	def visit(self, operator):
		return operator.success(TString(self.tok.value).setMemory(operator))

	def __repr__(self):
		return f'{self.tok}'
##############################
class NoList(Visitor):
	def __init__(self, tok):
		self.elements = tok

	def visit(self, operator):
		return operator.success(TList(self.elements.value).setMemory(operator))

	def visit(self, operator):
		lValue = []

		for element_node in self.elements:
			lValue.append(operator.registry(element_node.visit(operator)))
		
		return operator.success(TList(lValue).setMemory(operator))

	def __repr__(self):
		return f'{self.elements}'
	
class NoDict(Visitor):
    def __init__(self, pares_chave_valor):
        self.pares = pares_chave_valor

    def visit(self, operator):
        dict_valores = {}
        
        for chave_node, valor_node in self.pares:
            chave = operator.registry(chave_node.visit(operator))
            if operator.error: return operator
            
            valor = operator.registry(valor_node.visit(operator))
            if operator.error: return operator
            
            # Verificar se a chave é hashable
            if not isinstance(chave, (TNumber, TString)):
                return operator.fail(Error(f"{Error.runTimeError}: Chave do dicionário deve ser um número ou string"))
            
            dict_valores[chave] = valor
        
        return operator.success(TDict(dict_valores).setMemory(operator))

    def __repr__(self):
        return f'{{{self.pares}}}'