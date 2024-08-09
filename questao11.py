nomes = [""] * 5  
precos = [0.0] * 5  

for i in range(5):
    nome = input(f"Nome do medicamento {i+1}: ")
    preco = float(input(f"Preço do medicamento {i+1}: "))
    nomes[i] = nome  
    precos[i] = preco  

menor_preco = precos[0]  
indice_menor_preco = 0  

for i in range(1, 5):
    if precos[i] < menor_preco:
        menor_preco = precos[i]
        indice_menor_preco = i


medicamento_mais_barato = nomes[indice_menor_preco]


soma_precos = 0.0
for preco in precos:
    soma_precos += preco
media_precos = soma_precos / 5


print("Medicamento mais barato:", medicamento_mais_barato, "- R$", "{:.2f}".format(menor_preco))
print("Média dos preços: R$", "{:.2f}".format(media_precos))
