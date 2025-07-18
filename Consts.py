import string

class Consts:
    DIGITOS = '0123456789'
    LETRAS = string.ascii_letters
    LETRAS_DIGITOS = DIGITOS + LETRAS
    UNDER = '_'
    INT       = 'INT'
    FLOAT     = 'FLOAT'
    PLUS      = 'PLUS'      # Mudou de '+' para 'PLUS'
    MINUS     = 'MINUS'     # Mudou de '-' para 'MINUS'
    MUL       = 'MUL'       # Mudou de '*' para 'MUL'
    DIV       = 'DIV'       # Mudou de '/' para 'DIV'
    LPAR      = 'LPAR'      # Mudou de '(' para 'LPAR'
    RPAR      = 'RPAR'      # Mudou de ')' para 'RPAR'
    EOF       = 'EOF'       # Mudou de '$EOF' para 'EOF'
    EQ        = 'EQ'        # Mudou de '=' para 'EQ'
    POW       = 'POW'       # Mudou de '^' para 'POW'
    ID	      = 'ID'
    KEY		  = 'KEY'
    NULL      = 'null'
    STRING    = "STRING"
    GRAPH     = '@'
    LSQUARE   = "LSQUARE"   # Mudou de "[" para "LSQUARE"
    RSQUARE   = "RSQUARE"   # Mudou de "]" para "RSQUARE"
    COMMA     = "COMMA"     # Mudou de "," para "COMMA"
    LBRACE    = 'LBRACE'    # Mudou de '{' para 'LBRACE'
    RBRACE    = 'RBRACE'    # Mudou de '}' para 'RBRACE'
    COLON     = 'COLON'     # Mudou de ':' para 'COLON'

    # Símbolos para comparação no lexer
    PLUS_SYMBOL = '+'
    MINUS_SYMBOL = '-'
    MUL_SYMBOL = '*'
    DIV_SYMBOL = '/'
    LPAR_SYMBOL = '('
    RPAR_SYMBOL = ')'
    EQ_SYMBOL = '='
    POW_SYMBOL = '^'
    LSQUARE_SYMBOL = "["
    RSQUARE_SYMBOL = "]"
    COMMA_SYMBOL = ","
    LBRACE_SYMBOL = '{'
    RBRACE_SYMBOL = '}'
    COLON_SYMBOL = ':'

    # Exemplos de Palavras reservadas
    LET         = 'let'
    IF          = 'if'
    WHILE       = 'while'
    FOR         = 'for'
    KEYS = [
        LET,
        IF,
        WHILE,
        FOR
    ]