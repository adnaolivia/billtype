
class TestesTriangulo():

    def __init__(self, tipo_triangulo_func):
        self.tipo_triangulo = tipo_triangulo_func

    # Teste 1: Triângulo Equilátero
    def teste_triangulo_equilatero(self):
        a = 5
        b = 5
        c = 5
        resultado = self.tipo_triangulo(a, b, c)
        assert resultado == "Equilátero", f"Erro no teste de equilátero: resultado = {resultado}"
        print("Teste Equilátero passou!")


    # Teste 2: Triângulo Isósceles
    def teste_triangulo_isosceles(self):
        a = 5
        b = 5
        c = 3
        resultado = self.tipo_triangulo(a, b, c)
        assert resultado == "Isósceles", f"Erro no teste de isósceles: resultado = {resultado}"
        print("Teste Isósceles passou!")


    # Teste 3: Triângulo Inválido
    def teste_triangulo_invalido(self):
        a = 1
        b = 2
        c = 3
        resultado = self.tipo_triangulo(a, b, c)
        assert resultado == "Não é um triângulo válido", f"Erro no teste de triângulo inválido: resultado = {resultado}"
        print("Teste Triângulo Inválido passou!")