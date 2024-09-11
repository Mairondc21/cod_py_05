import pandas as pd

class CsvProcessor():
    def __init__ (self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    
    def carregar_csv (self):
        self.df = pd.read_csv(self.file_path)

##recebo somente uma str
    def filtrar_por(self,coluna,atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado
    
    ##recebo mais de uma str[]
    def filtrar_por_mais_de_um(self,colunas,atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Nao tem o mesmo numero de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtardo = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtardo
        else:
            return self.filtrar_por(colunas[1], atributos[1])
        
    

    def sub_filtro(self,coluna,atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]



arquivo_csv = "../dados/exemplo.csv"
filtro = 'estado'
limite = 'SP'

meu_csv = CsvProcessor(arquivo_csv)

meu_csv.carregar_csv() 
##print(meu_csv.filtrar_por(filtro,limite))
##print(meu_csv.sub_filtro('preço','10,50'))
print(meu_csv.filtrar_por_mais_de_um(['estado','preço'],['SP','10,50']))