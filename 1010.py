codigo1, qtd1, valor1 = input().split()
codigo2, qtd2, valor2 = input().split()

total = int(qtd1) * float(valor1) + int(qtd2) * float(valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
