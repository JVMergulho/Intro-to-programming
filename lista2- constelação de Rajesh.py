num= int(input())
check_fib=False
primo=True
n_pertence=0
soma=0
  
if num<=0:
  print('Isso está quebrado, acho que Howard pode me ajudar.')
elif 0<num<3:
  print('Acho que bebi demais, eu juro que tinha mais estrelas!')

else:
  for i in range(1,num):
    
    if i==1:
      x_anterior=int(input())
      y_anterior=int(input())
    
    x_atual=int(input())
    y_atual=int(input())
    
    dist= int(((x_atual-x_anterior)**2+(y_atual-y_anterior)**2)**(1/2))
    
    soma+=dist
    
    x_anterior=x_atual
    y_anterior=y_atual
    
    fib_ant1=1
    fib_ant2=1
    fib=1
    
    # Compara a distância com números de fibonacci 
    while dist>=fib:
      
      if dist==fib:
        check_fib=True
      fib=fib_ant1+fib_ant2
      
      fib_ant2=fib_ant1
      fib_ant1=fib
      
    print(f'Distância [star{i} <-> star{i+1}]: {dist}')
    
    if not check_fib:
      n_pertence+=1
    
    check_fib=False
    
  for div in range(2,soma):
    if soma%div==0:
      primo=False
    
  if n_pertence==0:
    if not primo:
      print('Yes! Eu consegui!')
    
    else:
      print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
  elif n_pertence==1:
    print('Oh, não! Eu quase consegui!')
    
  elif n_pertence>=1:
    if not primo:
      print('Eu vou acabar como o Stuart :/')
    else:
      print('Pelo menos o programa está funcionando...')
    
