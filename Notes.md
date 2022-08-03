![python](https://user-images.githubusercontent.com/50535434/182707744-a57a09e6-f1ab-4d8a-bc6f-39526e03ef86.gif)

---

Aula 7- Listas

Uma lista é uma estrutura de dados que armazena uma coleção ordenada de itens. Seus elementos veem entre '[ ]'.

A função ``len`` pode ser usada para calcular o tamanho de uma lista (número de itens)

```
lista_mercado = ['pão','quejo','leite']

tamanho_lista = len(lista)
```

Ela é uma estrutura _**iterável**_. Podemos usar comandos como o ``for`` para percorrê-la

```
for item in lista_mercado:
  print(f'você precisa comprar {item}')
```

Também é uma estrutura _**mutável**_. Podemos inserir e remover ítens, de modo a mudar o tamanho da lista.
O método ``append`` é usado para adicionar um elemento à lista.

```
lista_mercado.append('geleia')
```
Agora, a lista passa a ser ['pão','quejo','leite','geleia']

Usa-se índices para acessar um elemento específico da lista:

```
                  0      1       2       3
lista_mercado= ['pão','quejo','leite','geleia']
                 -4     -3      -2      -1
  
print(lista_mercado[0]) #saída: 'pão'
print(lista_mercado[-1]) #saída: 'geleia'
```

Com o ``slicing`` nós acessamos um intervalo do conteúdo da lista

```
print(lista_mercado[1:3])
```
Saída: ['quejo','leite']

Começa no índice 1 e vai até o índice anterior ao 3


```
print(lista_mercado[:3])
```
Saída: ['pão','quejo','leite']

Começa no índice 0 e vai até o índice anterior ao 3


