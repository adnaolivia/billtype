# Descrição do Fluxograma:
### Início (st3):

O fluxo começa com o início da função tipo_triangulo. Aqui, o programa está prestes a receber os dados de entrada.

### Entrada de dados (io5):

O programa solicita a entrada de três valores: os lados a, b e c do triângulo. Isso ocorre na etapa input: a, b, c.

### Verificação se é um triângulo válido (cond9):

O próximo passo é verificar se a soma de dois lados é sempre maior que o terceiro lado, o que é uma condição necessária para que os três valores formem um triângulo. A condição é:

```
(a + b > c) and (a + c > b) and (b + c > a)
```
Se a condição for verdadeira (ou seja, os valores formam um triângulo válido), o fluxo segue para a próxima verificação. Caso contrário, ele vai para a parte que imprime "Não é um triângulo válido" (sub37).

### Verificação de triângulo equilátero (cond14):

Se a condição do triângulo ser válido for atendida, o próximo passo é verificar se todos os três lados são iguais, o que caracteriza um triângulo equilátero. A condição é:

```
a == b == c
```
Se for verdadeiro, imprime "Equilátero" e o fluxo termina (sub18 -> e40).

### Verificação de triângulo isósceles (cond23):

Se o triângulo não for equilátero, o próximo passo é verificar se pelo menos dois lados são iguais, o que caracteriza um triângulo isósceles. A condição é:

```
(a == b) or (b == c) or (a == c)
```
Se for verdadeiro, o programa imprime "Isósceles" e termina (sub27 -> e40).
Caso contrário, é um triângulo escaleno (sub31):

Se o triângulo não for equilátero nem isósceles, o fluxo segue para a parte em que o programa imprime "Escaleno" (sub31 -> e40).

### Caso não seja um triângulo válido (sub37):

Se a verificação inicial (se os lados formam um triângulo válido) não for atendida, o programa imprime "Não é um triângulo válido" (sub37) e termina.

### Fim (e40):
O fluxograma termina em e40, que é o ponto de término da função tipo_triangulo.

# Explicação do Fluxo:
O fluxo começa com a coleta dos dados de entrada (os lados do triângulo).
O primeiro ponto crítico no fluxo é a verificação se os lados formam um triângulo válido.
Se a condição for atendida, o fluxo passa por várias verificações para determinar o tipo do triângulo (equilátero, isósceles ou escaleno).
Se a condição não for atendida, o fluxo imprime "Não é um triângulo válido".
Finalmente, o programa imprime o tipo de triângulo ou uma mensagem de erro, e o processo é encerrado.
Este fluxograma ajuda a visualizar a sequência de decisões e ações dentro da função tipo_triangulo do código, tornando mais fácil entender o fluxo lógico do programa.