## Gerenciamento de Dados do Usuário

Este programa Python fornece funções para coletar e armazenar informações do usuário, como nome, endereço e telefone. As informações coletadas são então impressas na tela.

## Funcionalidades

* Função `ler_nome()`:**
    * Solicita ao usuário que digite seu nome.
    * Retorna o nome digitado como uma string.
* Função `ler_endereco()`:**
    * Solicita ao usuário que digite seu endereço.
    * Retorna o endereço digitado como uma string.
* Função `ler_telefone()`:**
    * Solicita ao usuário que digite seu telefone.
    * Retorna o número de telefone digitado como uma string.
* Função principal (`main()`):**
    * Chama as funções `ler_nome()`, `ler_endereco()` e `ler_telefone()` para coletar as informações do usuário.
    * Imprime o nome, endereço e telefone do usuário na tela.

### Exemplo de Uso

```python
nome = ler_nome()
endereco = ler_endereco()
telefone = ler_telefone()

print(f"Nome: {nome}")
print(f"Endereço: {endereco}")
print(f"Telefone: {telefone}")
```

## Observações

* Este código pode ser facilmente adaptado para outros propósitos de coleta de dados.
* As funções podem ser modificadas para validar e formatar os dados coletados.
* O código pode ser integrado a outros programas para gerenciar informações do usuário de forma eficiente.

## Melhorias Futuras

* Implementar validação de entrada para garantir que os dados sejam digitados nos formatos corretos.
* Adicionar opções para salvar os dados do usuário em um arquivo ou banco de dados.
* Criar uma interface gráfica do usuário para facilitar a coleta de dados.
