cod1, numpec1, valor1 = input().split()
cod2, numpec2, valor2 = input().split()

cod1 = int(cod1)
numpec1 = int(numpec1)
valor1 = float(valor1)

cod2 = int(cod2)
numpec2 = int(numpec2)
valor2 = float(valor2)

total = (numpec1 * valor1) + (numpec2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")