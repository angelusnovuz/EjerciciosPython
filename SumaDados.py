from random import *

def suma(d1, d2):
    return d1 + d2

def comentario(dado1, dado2):
    return print(f"El dado uno es: {dado1}, y el dado dos es: {dado2}\n La suma de los dados es: {suma(dado1,dado2)}")

dado1 = randint(1,6)
dado2 = randint(1,6) 

print("----------------- TIRANDO DADOS ----------------")
comentario(dado1,dado2)

valor = input(str(("Quisiera seguir jugando? 'si' para continuar o 'no' para terminar: ")))

while valor != 'no':
    if valor == 'si':
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        comentario(dado1,dado2)
    else:
        print("\n ERROR, INGRESAR UN VALOR CORRECTO \n")
        
    valor = input(str(("Quisiera seguir jugando? 'si' para continuar o 'no' para terminar: ")))
    
print("Gracias por jugar, vuelva pronto")
