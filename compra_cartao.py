print("Exercicio sobre compra no cartão\n")

credito = float(input("Seu crédito: "))
total = 0 #variável acumuladora

preco = float(input("\nPreço do produto: "))
while (credito >= preco):
    total+= preco
    credito -= preco

    print(f"O Total é de R$ {total:.2f} e seu Crédito é de R${credito:.2f}")

    continuar = input("\nDeseja continuar comprando? ")
    if (continuar != "sim" and continuar != "s"):
        break

    preco = float(input("\nPreço do Produto: "))
    if (preco > credito):
        print("\nSaldo insuficiente")
        break


print(f"\nO Total da compra foi de: R$ {total:.2f}")
print(f"Seu Crédito restante é de: R$ {credito:.2f}")