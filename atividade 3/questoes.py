def questao_1():
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = num1 / num2

    except ValueError:
        print("Entrada invalida! Digite apenas numeros")
    except ZeroDivisionError:
        print("Impossivel dividir por zero.")
    else:
        print(f"O resultado da divisao: {resultado}")
    
    return questao_1

def questao_2():
    
   quantidade = int(input("Digite a quantidade de notas que voce deseja inserir: "))

   notas = []

   for i in range(quantidade):
       nota = float(input("Digite a nota: "))
       notas.append(nota)

   media = sum(notas) / len(notas)
   print(f"Notas: {notas}\nMedia: {media:.2f}")
   
   return questao_2

def questao_3():
    
    horas_semanal = []

    for i in range(7):
        quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))
        horas_semanal.append(quantidade_horas)

    total_semanal = sum(horas_semanal)

    if total_semanal >= 40:
        print("Carga completa.")
    else:
        print("Carga incompleta.")
        
    return questao_3

def questao_4():
    try:
        saldo = float(input("Digite o seu valor de saldo atual: R$ "))
        while True: 
            print("\n1- Deposito")
            print("2- Saque")
            print("3- Sair")
            
            opcao = input("\nEscolha uma opcao: ")
            
            if opcao == '1':
                deposito = float(input("Digite o seu valor de deposito: R$ "))
                saldo_atual = saldo + deposito
                print(f"Valor atual em conta: R$ {saldo_atual}")
            
            elif opcao == '2':
                saque = float(input("Digite o seu valor de saque: R$ "))
                saldo_atual = saldo - saque
                print(f"Valor atual em conta: R$ {saldo_atual}")

            elif opcao == '3':
                print("Ate logo.")
                break

            else:
                print(f"Opcao invalida.")

    except ValueError:
        print("Entrada invalida, digite apenas numeros.")
    
    return questao_4


def questao_5():

    nomes = []
    notas = []
    aprovados = []

    quantidade = int(input("Digite a quantidade de alunos: "))

    for i in range(quantidade):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
        nomes.append(nome)

        if nota >= 7:
            aprovados.append((nome, nota))

    print(f"\nLista de aprovados: ")
    for nome, nota in aprovados:
        print(f"{nome}: {nota}")

    return questao_5
