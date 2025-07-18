class Util():
    @staticmethod
    def readFile(filename: str):
        res = ""
        try:
            with open(filename, 'r') as f: res = f.read()
        except IOError:
            print("Erro ao ler arquivo!!")
            return ""
        return res
    
    @staticmethod
    def writeFileAppend(filename: str, content: str):
        try:
            with open(filename, 'a+') as f: f.write(content)

        except IOError:
            print("Erro ao gravar no arquivo!!")

    @staticmethod
    def createFile(filename: str):
        try:
            with open(filename, 'w') as f: f.write("")

        except IOError:
            print("Erro ao gravar no arquivo!!")

