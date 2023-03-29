'''Esse código em Python pede ao usuário que ele insira um número para o qual a tabuada deve ser exibida. Em seguida,
ele utiliza um loop "while" para iterar de 1 a 10 e exibe uma tabuada correspondente ao número digitado.
A cada iteração do loop, o código multiplica o número inserido pelo usuário  e exibe o resultado formatado em uma string
usando a função "print".'''

n =int(input("De qual numero você quer a tabuada?"))
i= 1
while i <=10:
    print("{} x {} = ={}".format(n, i,n * i))
    i= i + 1
