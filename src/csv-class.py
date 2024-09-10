import pandas as pd

class CsvProcessor():
    def __init__ (self, file_path: str):
        self.file_path = file_path
        self.df = None

    
    def carregar_csv (self):
        self.df = pd.read_csv(self.file_path)


    def filtrar_por(self,coluna,atributo):
        return self.df[self.df[coluna] == [atributo]]


arquivo_csv = "../dados/exemplo.csv"
filtro = 'estado'
limite = 'SP'

meu_csv = CsvProcessor(arquivo_csv)

meu_csv.carregar_csv() 
print(meu_csv.filtrar_por(filtro,limite))