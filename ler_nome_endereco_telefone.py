# Função para ler o nome
def ler_nome():
  """
  Função para ler o nome do usuários.
  Retorna:
  str: O nome do usuário.
  """
  nome = input("Digite o seu nome: ")
  return nome


  # Função para ler o endereço
def ler_endereco():
  """
  Função para ler o endereço do usuário.
  Retorna:
  str: O endereço do usuário.
  """
  endereco = input("Digite o seu endereço: ")
  return endereco


  # Função para ler o telefone
def ler_telefone():
  """
  Função para ler o telefone do usuário.
  Retorna:
  str: O telefone do usuário.
  """
  telefone = input("Digite o seu telefone: ")
  return telefone
  # Função principal para ler o nome, endereço, telefone e imprimir na tela.


nome = ler_nome()
endereco = ler_endereco()
telefone = ler_telefone()
# Imprimir os dados do usuário
print(f"Nome: {nome}")
print(f"Endereço: {endereco}")
print(f"Telefone: {telefone}")
if __name__ == "__main__":
  main()
