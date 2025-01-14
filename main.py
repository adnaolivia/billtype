from testes import TestesTriangulo

def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo válido"

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

resultado = tipo_triangulo(a, b, c)

print(f"O triângulo é: {resultado}")

testes = TestesTriangulo(tipo_triangulo)
testes.teste_triangulo_equilatero()
testes.teste_triangulo_isosceles()
testes.teste_triangulo_invalido()