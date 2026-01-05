A, B, C = map(float, input().split())
n = 3.14159

a1 = (A * C) / 2
a2 = n * (C ** 2)
a3 = ((A + B) * C) / 2
a4 = B * B
a5 = A * B

print(f"TRIANGULO: {a1:.3f}")
print(f"CIRCULO: {a2:.3f}")
print(f"TRAPEZIO: {a3:.3f}")
print(f"QUADRADO: {a4:.3f}")
print(f"RETANGULO: {a5:.3f}")