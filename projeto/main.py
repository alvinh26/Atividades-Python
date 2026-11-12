from config.db import criar_conexao
from servicos.services import inserir_paciente, cadastro_paciente
from servicos.validacao import validar_cpf, validar_telefone

conexao = criar_conexao()

while True:
    print("1- Inserir paciente\n2- Listar pacientes\n3- Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Insira os dados do paciente: ")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = int(input("Telefone: "))
        cpf = int(input("CPF: "))
        inserir_paciente(nome, endereco, telefone, cpf)
        
        if validar_telefone:
            print("Telefone já cadastrado. Insira outro telefone.")
            continue
        if validar_cpf:
            print("CPF já cadastrado.")
            continue

    elif opcao == 2:
        nome = input("Digite o nome do paciente que você deseja procurar: ")
        endereco = input("Digite o endereço desse paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        cpf = input("Digite o cpf do paciente: ")
        pacientes = cadastro_paciente(nome, endereco, telefone, cpf)
        if pacientes:
            for paciente in pacientes:
                print(paciente)
        else:
            print("Paciente inválido")
    elif opcao == 3:
        break
    
    else:
        print("Opção inválida. Tente novamente.")