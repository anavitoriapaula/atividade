# Função para calcular a soma dos números inteiros no intervalo [a, b]
def soma_intervalo(a, b):
    return sum(range(a, b + 1))

# Solicitar entrada do usuário
try:
    a = int(input("Digite o primeiro número inteiro (a): "))
    b = int(input("Digite o segundo número inteiro (b): "))

    # Verificar se a < b
    if a < b:
        resultado = soma_intervalo(a, b)
        print(f"A soma dos números inteiros no intervalo [{a}, {b}] é {resultado}.")
    else:
        print("Erro: o primeiro número deve ser menor que o segundo número.")
except ValueError:
    print("Erro: entrada inválida. Por favor, insira apenas números inteiros.")
