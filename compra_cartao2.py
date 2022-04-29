print("Exercicio sobre compra no cartão\n")

credito = float(input("Seu crédito: "))
total = 0

continua = input("\nDeseja comprar?")
if continua == "s" or continua == "sim":
    while True:
        preco = float(input("\nPreço do produto: "))
        if (preco <= credito):
            print("Compra aprovada")
            total += preco
            credito -= preco

            print(f"\nO Total é de R$ {total:.2f} e seu Crédito é de R${credito:.2f}")

            continuar = input("\nDeseja continuar comprando? ")
            if (continuar != "s" and continuar != "sim"):
                break
        else:
            print("Saldo Inválido")
            print(f"Seu Crédito restante é de: R$ {credito:.2f}")
            continue
else:
    print("\nOk! Tenha um bom dia!")
    print(f"Seu Crédito restante é de: R$ {credito:.2f}")

if total != 0:
    print(f"\nO Total da compra foi de: R$ {total:.2f}")
    print(f"Seu Crédito restante é de: R$ {credito:.2f}")

