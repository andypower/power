ele=0
insieme = set()
for z in range(7):
  for y in range(7):  
    for x in range(7):  
      for k in range(7):  
        for j in range(7):  
          for i in range(7):  
            if i+j+k+x+y+z == 6:
              lista = list()
              lista.append(i)
              lista.append(j)
              lista.append(x)
              lista.append(y)
              lista.append(z)
              lista.append(k)
              lista.sort()
              
              listaPulita=[w for w in lista if w!=ele]
              
              stringa = ''.join(str(e) for e in listaPulita)
              insieme.add(stringa)

              
print('Elementi del set', len(insieme), insieme)
