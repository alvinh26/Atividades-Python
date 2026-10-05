from validacao import pedir_texto, pedir_preco, pedir_inteiro

def registrar_alimento(alimentos):
    titulo = pedir_texto(f"Titulo (mínimo de 2 caracteres): ", 2)
    preco = pedir_preco("Preço: ")
    descricao = pedir_texto(f"Descrição (mínimo de 5 caracteres): ", 5)

    alimento = {"titulo": titulo, "preco": preco, "descricao": descricao}
    alimentos.append(alimento)
    print("Alimento registrado!")

def listar_alimento(alimentos):
    if len(alimentos) == 0:
        print("Nenhum alimento registrado.")
        return
    for alimento in alimentos:
        print(f"- {alimento['titulo']} | R$ {alimento['preco']}\n {alimento['descricao']}")

def registrar_venda(alimentos, vendas):
    if len(alimentos) == 0:
        print("Nenhum alimento para vender.")
        return
    for i in range(len(alimentos)):
        print(f"{i+1} - {alimentos[i]['titulo']} | R$ {alimentos[i]['preco']}")
    numero = pedir_inteiro("Número do alimento vendido: ", 1, len(alimentos))
    quantidade = pedir_inteiro("Quantidade vendida: ", 1, 1000)    
    alimento = alimentos [numero - 1]
    total = alimento["preco"] * quantidade

    venda = {"titulo":alimento['titulo'], "quantidade":quantidade, "total":total}
    vendas.append(venda)
    print(f"Venda registrada. Total: R$ {total:.2f}")

def menu_alimentos(alimentos, vendas):
    while True:
        print(f"\n1- Regristrar alimento\n2- Listar alimentos\n3- Registrar venda\n4- Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_alimento(alimentos)
        elif opcao == '2':
            listar_alimento(alimentos)
        elif opcao == '3':
            registrar_venda(alimentos, vendas)
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")
