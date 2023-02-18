ele=0
insieme = set()
for z in range(11):
  for y in range(10):  
    for x in range(9):  
      for k in range(8):  
        for j in range(7):  
          for i in range(6):
            for a in range(5):
              for b in range(4):
                for c in range(3):
                  for d in range(2):
                    if i+j+k+x+y+z+a+b+c+d == 10:
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
                      lista.append(d)
                      lista.sort()
                      
                      listaPulita=[w for w in lista if w!=ele]
                      
                      stringa = ''.join(str(e) for e in listaPulita)
                      insieme.add(stringa)

              
print('Elementi del set', len(insieme), insieme)
