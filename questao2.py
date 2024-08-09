def imprimir_pa(primeiro_termo, quantidade_termos, razao):
    # Calcula e imprime cada termo da PA
    for i in range(quantidade_termos):
        termo_atual = primeiro_termo + i * razao
        print(termo_atual, end=' ')
    print()  # Para adicionar uma nova linha após imprimir todos os termos

# Exemplo de uso
primeiro_termo = float(input("Informe o primeiro termo: "))
quantidade_termos = int(input("Informe a quantidade de termos: "))
razao = float(input("Informe a razão: "))

imprimir_pa(primeiro_termo, quantidade_termos, razao)

