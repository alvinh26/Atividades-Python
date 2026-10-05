from validacao import pedir_texto, pedir_email, pedir_inteiro
from alimentos import menu_alimentos

def buscar_usuario(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return usuario
        return None
    
def adicionar_usuario(usuarios):
    nome = pedir_texto("Nome: ", 3)
    email = pedir_email("Email: ")
    if buscar_usuario(usuarios, email) != None:
        print("Esse e-mail já está cadastrado.")
        return
    
    senha = pedir_texto("Senha: ", 4)
    novo = {"nome": nome, "email": email, "senha": senha}
    usuarios.append(novo)
    print("Usuário cadastrado.")

def registrar_compra(usuario, alimentos, vendas, compras):
    if len(alimentos) == 0:
        print("Nenhum alimento disponível para compra.")
        return

    for i in range(len(alimentos)):
        print(f"{i+1} - {alimentos[i]['titulo']} | R$ {alimentos[i]['preco']}")

    numero = pedir_inteiro("Número do alimento que deseja comprar: ", 1, len(alimentos))
    quantidade = pedir_inteiro("Quantidade: ", 1, 1000)
    alimento = alimentos[numero-1]
    total = alimento['preco'] * quantidade

    compra = {
        "email": usuario['email'],
        "titulo": alimento['titulo'],
        "quantidade": quantidade,
        "total": total 
}
    compras.append(compra)

    venda = {"titulo": alimento['titulo'], "quantidade": quantidade, "total": total}
    vendas.append(venda)
    print(f"Compra registrada! Total: R$ {total: .2f}")


def menu_usuario(usuario, alimentos, vendas, compras):
    while True:
        print("\n1- Área de alimentos\n2- Comprar alimento\n3- Sair da conta")
        opcao = input("Escolha: ")

        if opcao == '1':
            menu_alimentos(alimentos, vendas)
        elif opcao == '2':
            registrar_compra(usuario, alimentos, vendas, compras)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

def entrar_sistema(usuarios, alimentos, vendas, compras):
    email = input("E-mail: ").strip()
    senha = input("Senha: ")
    usuario = buscar_usuario(usuarios, email)

    if usuario != None and usuario['senha'] == senha:
        print(f"Bem-vindo {usuario['nome']}")
        menu_usuario(usuario, alimentos, vendas, compras)
    else:
        print("E-mail ou senha incorretos.")