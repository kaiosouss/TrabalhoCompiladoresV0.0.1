####################################### TOKENS #######################################
class Token:
    def __init__(self, tipo, valor=None):
        self.type = tipo
        self.value = valor

    def matches(self, _type, _value):
        return self.type == _type and self.value == _value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
