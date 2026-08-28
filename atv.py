cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]
print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")


for i in range(len(cadastros_brutos)):
   for i in range(len(cadastros_brutos)):

   
    cadastro = cadastros_brutos[i].strip()


    nome, telefone = cadastro.split(";")

    
    nome = nome.upper()

    
    ddd = telefone[0:2]

    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")


print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")