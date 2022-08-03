
<img src= "https://user-images.githubusercontent.com/50535434/182708414-ba308f44-5524-420f-af04-0c6b50faab09.gif" width="350" height="350"> 

---

# Aula 7- Listas

### Definição

Uma lista é uma estrutura de dados que armazena uma coleção ordenada de itens. Seus elementos veem entre '[ ]'. Ela pode armazenar elementos de tipos diferentes de forma simultânea

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

Também é uma estrutura _**mutável**_. Podemos inserir e remover itens, de modo a mudar o tamanho da lista.
O método ``append(item)`` é usado para adicionar ``item `` à lista.

```
lista_mercado.append('geleia')
```
Agora, a lista passa a ser ['pão','queijo','leite','geleia']

### Indexação/Slicing

Usa-se índices para acessar um elemento específico da lista:

```
                  0      1       2       3
lista_mercado= ['pão','queijo','leite','geleia']
                 -4     -3      -2      -1
  
print(lista_mercado[0]) #saída: 'pão'
print(lista_mercado[-1]) #saída: 'geleia'
```

Com o ``slicing`` nós acessamos um intervalo do conteúdo da lista

```
print(lista_mercado[1:3])
```
Saída: ['queijo','leite']

Começa no índice 1 e vai até o índice anterior ao 3


```
print(lista_mercado[:3])
```
Saída: ['pão','queijo','leite']

### Busca

Começa no índice 0 e vai até o índice anterior ao 3

O método ``index(item,inicio)`` faz uma busca por um elemento na lista e retorna o index de sua primeira ocorrência.  Ele recebe o item a ser procurado e o índex de início da busca (facultativo).

```
index_leite= lista_mercado.index('leite')
```
Saída: 2

### Sorting

O método ``sort`` ordena os elementos - em ordem alfabética no caso de strings e do menor para o maior no caso de números. ``sort(reverse=True)`` ordena de forma inversa. Importante: ela modifica a lista em si!!

```
lista_abc=['a','c','b','f','e']
lista_abc.sort()
print(lista)
```
Saída: ['a','b','c','e','f']

Já a função ``sorted`` cria uma nova lista ordenada e não modifica a original.

```
lista_nova= sorted(lista_abc)
print(lista_nova)
```
Saída: ['a','b','c','e','f']

### Inserção/Remoção de elementos

Além de ``append`` pode-se usar ``insert(idx,valor)`` para inserir um elemento. Esse método insere ``valor`` no índex ``idx``

```
lista_nova.insert(3,'d')
print(lista_nova)
```
Saída: ['a','b','c','d','e','f']

A função ``remove(valor)`` remove a primeira ocorrência de ``valor``

Para remover e retornar ``valor`` como resultado usamos ``pop(valor)``

```
lista_nova.remove('a')
print(lista_nova.pop('b'))
```
Saída: 'b'

### Fundir listas

Pode-se usar a operação de concatennação para "juntar" os elementos de duas listas.

```
listaA=[1,2,3]
listaB=[4,5,6]

listaAB= listaA+listaB

print(listaAB)
```
saída: [1,2,3,4,5,6]

### Replace

A função ``replace(arg1,arg2)`` substitui todas as ocorrências do ``arg1`` por ``arg2`` em uma string

```
texto= '+b+c+te'
texto= texto.replace('+','a')
print(texto)
```
Saída: 'abacate'
