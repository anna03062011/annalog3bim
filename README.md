dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]
def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Deve receber uma string.
   - Deve remover espaços extras das pontas (.strip()).
   - Deve converter o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   texto_limpo = texto.strip()
   texto_formatado = texto_limpo.upper()
   return texto_formatado


def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Deve receber um dado em formato de string (ex: telefone ou CPF).
   - Deve remover espaços das pontas.
   - Deve utilizar FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros dígitos (ex: DDD).
   - Retorna apenas os dígitos extraídos.
   """
   dado_limpo = dado.strip()
   codigo = dado_limpo[0:2]
   return codigo


def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Deve receber a lista de cadastros brutos como parâmetro.
   - Deve utilizar um laço FOR para percorrer cada item da lista.
   - Em cada iteração do for:
       1. Separar as partes usando .split(";")
       2. Chamar a Função 1 para formatar o Nome e o Cargo.
       3. Chamar a Função 2 para extrair o DDD/Código do telefone.
       4. Exibir o resultado final formatado na tela com f-string.
   - Retorna a quantidade total de registros processados.
   """
   contador = 0

   for registro in lista_dados:
        partes = registro.split(";")
       nome_bruto = partes[0]
       cargo_bruto = partes[1]
       telefone_bruto = partes[2]

      nome_formatado = limpar_e_formatar_texto(nome_bruto)
       cargo_formatado = limpar_e_formatar_texto(cargo_bruto)

       ddd = extrair_codigo_ou_ddd(telefone_bruto)

       print(f"Nome: {nome_formatado} | Cargo: {cargo_formatado} | DDD: {ddd}")

       contador += 1

   return contador

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

     total_processado = processar_e_exibir_cadastros(dados_brutos)

  print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")

if __name__ == "__main__":
   main()
