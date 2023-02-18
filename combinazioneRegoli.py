ele=0
insieme = set()
for z in range(10):
  for y in range(9):  
    for x in range(8):  
      for k in range(7):  
        for j in range(6):  
          for i in range(5):
            for a in range(4):
              for b in range(3):
                for c in range(2):
            if i+j+k+x+y+z+a+b+c == 9:
              lista = list()
              lista.append(i)
              lista.append(j)
              lista.append(x)
              lista.append(y)
              lista.append(z)
              lista.append(k)
              lista.append(a)
              lista.append(b)
              lista.append(c)
              lista.sort()
              
              listaPulita=[w for w in lista if w!=ele]
              
              stringa = ''.join(str(e) for e in listaPulita)
              insieme.add(stringa)

              
print('Elementi del set', len(insieme), insieme)
