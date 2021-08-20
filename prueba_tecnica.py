from datetime import datetime

# Retorna True si el numero validado es "rebotante" de lo contrario retorna False
def is_bouncy(dato):
    if(int(dato)<100): return False
    else: 
        digito_anterior = dato[0]
        estado = None
        for digito in dato[1:]: 
            if((digito > digito_anterior and estado=="disminuye") or (digito < digito_anterior and estado=="aumenta")): 
                return True
            elif(digito>digito_anterior): estado="aumenta"
            elif(digito<digito_anterior): estado="disminuye"
            digito_anterior = digito    
        return False

def count_is_bouncy(valor, total_bouncy=0):
    proportion_bouncy = 0
    if(is_bouncy(str(valor))): total_bouncy+=1
    proportion_bouncy = (total_bouncy/valor)*100

    return (total_bouncy, proportion_bouncy)

def main():
    proporcion = int(input("Digite la proporcion de numeros rebotantes a validar (%):"))
    continuar = True
    numero = 101
    count_bouncy = 0
    tiempo_inicial = datetime.now()
    print("\n", tiempo_inicial, "Inicia el procesamiento...")
    while(continuar):
      count_bouncy, porcentaje = count_is_bouncy(numero, count_bouncy)
      if(porcentaje >= proporcion):
        print("\nValor:", numero)
        print("Total rebotantes:", count_bouncy)
        print("Total NO rebotantes:", numero-count_bouncy)
        print("Porcentaje rebotantes:", porcentaje, "%")
        print("Tiempo de procesamiento:", datetime.now()-tiempo_inicial)
        continuar=False
      else: numero+=1
      
    print("\n", datetime.now(), "Finaliza el procesamiento")  

if __name__ == "__main__":
    main()