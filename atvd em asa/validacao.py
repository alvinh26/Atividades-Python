def pedir_texto(mensagem, minimo):
    while True:
        texto = input(mensagem).strip()
        if len(texto)>= minimo:
            return texto
        print(f"Digite pelo menos {minimo} caracteres.")

def pedir_email(mensagem):
    while True:
        email = input(mensagem).strip()
        if "@" in email and "." in email:
            return email
        print(f"Digite um e-mail válido. (ex.: nome@email.com)")

def pedir_preco(mensagem):
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            preco = float(texto)
        except ValueError:
            print("Digite um número válido.")
            continue
        if preco > 0:
            return preco
        print("O preço tem que ser maior que zero.")

def pedir_inteiro(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"Digite um número entre {minimo} e {maximo}.")