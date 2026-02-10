import sys

def solucionar():
   
    for linea in sys.stdin:
        partes = linea.split()
        
        if not partes:
            continue
          
        n = int(partes[0])
        k = int(partes[1])

        suma_total = (n * (n + 1)) // 2
 
        if suma_total % k == 0:
            print("SI")
        else:
            print("NO")

if _name_ == "_main_": 
    solucionar()