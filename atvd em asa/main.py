from usuarios import adicionar_usuario, entrar_sistema

usuarios = []
alimentos = []
vendas = []
compras = []

while True:
    print("\n1- Adicionar usuários\n2- Entrar no sistema\n3- Sair")
    opcao = input("Escolha: ")

    if opcao =='1':
        adicionar_usuario(usuarios)
    elif opcao == '2':
        entrar_sistema(usuarios, alimentos, vendas, compras)
    elif opcao == '3':
        print("Até logo.")
        break
    else:
        print("Opção inválida.")