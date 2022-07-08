import pandas as pd

lista_nome = []
lista_idade = []
lista_sexo = []



for i in range(6):
    lista_nome.append(input("digite seu nome: "))
    lista_idade.append(input("digite sua idade: "))
    lista_sexo.append(input("digite seu sexo: "))

planilha = pd.DataFrame(
    {
        'nome': lista_nome,
        'idade': lista_idade,
        'sexo': lista_sexo

    }
)
planilha.to_excel('teste.xlsx', index=False)