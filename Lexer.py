from Consts import Consts
from Token import Token
from Error import Error

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.indice, self.coluna, self.linha = -1, -1, 0
        self.__advance()

    def __advance(self):
        self.__advanceCalc(self.current)
        self.current = self.code[self.indice] if self.indice < len(self.code) else None

    def __advanceCalc(self, _char=None):
        self.indice += 1
        self.coluna += 1
        if _char == '\n':
                self.linha += 1
                self.coluna = 0
        return self

    def makeTokens(self):
        tokens = []
        while self.current != None:
            if self.current in ' \t':
                self.__advance()
            elif self.current in Consts.DIGITOS:
                tokens.append(self.__makeNumber())
            elif(self.current == '"'):
                tokens.append(self.__MakeString())
            elif self.current == Consts.PLUS_SYMBOL:
                tokens.append(Token(Consts.PLUS))
                self.__advance()
            elif self.current == Consts.MINUS_SYMBOL:
                tokens.append(Token(Consts.MINUS))
                self.__advance()
            elif self.current == Consts.MUL_SYMBOL:
                tokens.append(Token(Consts.MUL))
                self.__advance()
            elif self.current == Consts.DIV_SYMBOL:
                tokens.append(Token(Consts.DIV))
                self.__advance()
            elif self.current == Consts.POW_SYMBOL:
                tokens.append(Token(Consts.POW))
                self.__advance()
            elif self.current == Consts.LPAR_SYMBOL:
                tokens.append(Token(Consts.LPAR))
                self.__advance()
            elif self.current == Consts.RPAR_SYMBOL:
                tokens.append(Token(Consts.RPAR))
                self.__advance()
            ##################################
            elif self.current in Consts.LETRAS + Consts.UNDER:
                tokens.append(self.__makeId())
            elif self.current == Consts.LSQUARE_SYMBOL:
                tokens.append(Token(Consts.LSQUARE))
                self.__advance()
            elif self.current == Consts.RSQUARE_SYMBOL:
                tokens.append(Token(Consts.RSQUARE))
                self.__advance()
            elif self.current == Consts.COMMA_SYMBOL:
                tokens.append(Token(Consts.COMMA))
                self.__advance()
            elif self.current == Consts.EQ_SYMBOL:
                tokens.append(Token(Consts.EQ))
                self.__advance()
            ##############################
            elif self.current == Consts.LBRACE_SYMBOL:
                tokens.append(Token(Consts.LBRACE))
                self.__advance()
            elif self.current == Consts.RBRACE_SYMBOL:
                tokens.append(Token(Consts.RBRACE))
                self.__advance()
            elif self.current == Consts.COLON_SYMBOL:
                tokens.append(Token(Consts.COLON))
                self.__advance()
            else:
                self.__advance()
                return [], Error(f"{Error.lexerError}: lex-symbol '{self.current}' fail!")

        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        strNumber = ''
        dotCount = 0
        while self.current != None and self.current in Consts.DIGITOS + '.':
            if self.current == '.':
                if dotCount == 1: break
                dotCount += 1
                strNumber += '.'
            else:
                strNumber += self.current
            self.__advance()

        if dotCount == 0:
            return Token(Consts.INT, int(strNumber))
        else:
            return Token(Consts.FLOAT, float(strNumber))
    
    def __MakeString(self):
        stri = ""
        bypass = False
        self.__advance()
        specialChars = {'n':'\n', 't': '\t'}
        while (self.current != None and (self.current != '"' or bypass)):
            if (bypass):
                c = specialChars.get(self.current, self.current)
                stri += c
                bypass = False
            else:
                if (self.current == '\\'):
                    bypass = True
                else:
                    stri += self.current
            self.__advance()

        self.__advance()
        return Token(Consts.STRING, stri)

    ##############################
    def __makeId(self):
        lexema = ''
        while self.current != None and self.current in Consts.LETRAS_DIGITOS + Consts.UNDER:
            lexema += self.current
            self.__advance()

        tokType = Consts.KEY if lexema in Consts.KEYS else Consts.ID
        return Token(tokType, lexema)
    ##############################
