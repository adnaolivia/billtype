import pyflowchart

code = '''
def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilátero")
        elif a == b or b == c or a == c:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("Não é um triângulo válido")

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

resultado = tipo_triangulo(a, b, c)

print(f"O triângulo é: {resultado}")
'''
flowchart = pyflowchart.Flowchart.from_code(code)
print(flowchart.flowchart())