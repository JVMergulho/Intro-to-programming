num= int(input())
decimal=0
binario=''
erros=0
acertos=0

for cont in range(num):
  operacao= input()
  
  #conversão de binário para decimal
  
  if operacao=='DEC':
    decimal=0
    valor= input() #valor é lido como uma string
    tamanho=len(valor)
    
    cont=1
    for bit in valor:
      if bit=='1':
        decimal+=2**(tamanho-cont)
      cont+=1
    
    palpite=int(input())
    
    if palpite==decimal:
      acertos+=1
    else:
      erros+=1
      print(f'Palpite Incorreto, o valor {valor} = {decimal}')
  
  #conversão de decimal para binário
  
  elif operacao=='BIN':
    valor= int(input()) #valor é lido como um inteiro
    binario=''
    
    conv=valor
  
    while conv>1:
      if conv%2==0:
        binario='0'+ binario
      else:
        binario='1'+ binario
      conv= int(conv/2)
      
    if conv==1:
      binario='1'+binario
    else:
      binario= '0'+binario
    
    palpite=input()
    
    if palpite==binario:
      acertos+=1
    else:
      erros+=1
      print(f'Palpite Incorreto, o valor {valor} = {binario}')

if acertos>erros:
  print('Bazinga! Quem realizou esses cálculos foi o computador??')
else:
  print('Parece que realizar conversões em binário não é o seu forte')
  
