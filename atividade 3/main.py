from questoes import questao_1, questao_2, questao_3, questao_4, questao_5


while True:
    print("\n1- Exibir primeira questao")
    print("2- Exibir segunda questao")
    print("3- Exibir terceira questao")
    print("4- Exibir quarta questao")
    print("5- Exibir quinta questao")
    print("6- Sair")
        
    opcao = input("\nEscolha uma opcao: ")

    if opcao == '1':
        questao_1()
    elif opcao == '2':
        questao_2()
    elif opcao == '3':
        questao_3()
    elif opcao == '4':
        questao_4()
    elif opcao == '5':
        questao_5()
    elif opcao == '6':
        print("Ate logo.")
        break    
    else:
        print("Opcao invalida.")