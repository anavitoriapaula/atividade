produtos = []
whlile True:
  produto = input("digite o nome do produto")
produtos.append(produto)
continuar = input("Deseja adicionar outro produto: (sim/não): ")
  if continuar upper()!= "sim":
    break
print("\nLista de produtos eletronocos: ")
for produto in produtos:
  print("-"+produto)
