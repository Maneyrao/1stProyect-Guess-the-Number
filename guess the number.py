import random    

    
def dificultad():
    while True:
        print("Choose difficulty: easy, medium, hard")
        difficulty = input("Enter difficulty: ").lower()
    
        if difficulty == "easy":
            return 1, 10
        elif difficulty == "hard":
            return 1, 50
        elif difficulty == "medium":
            return 1, 22    
        else:
            print("dificultad inválida, elegí una de las opciones que te ofrecí pa")

def juego():
    min_num, max_num = dificultad()
    random_number = random.randint(min_num, max_num)  # Generar nuevo número
    intentos = 0
    while True:
        try:
            intento = int(input(f"a ver rey, decime un número entre {min_num} y {max_num}: "))
            intentos += 1
        except ValueError:  
            print("Por favor, ingresa un número válido.")
            continue
        if not min_num <= intento <= max_num:
            print(f"El número debe estar entre {min_num} y {max_num}.")
            continue
            
        if intento == random_number:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos")
                continuar = input("quieres seguir jugando? (Si/No): ").lower()
                if continuar != "si":
                    print("adios makina del bien")
                    break
                else:
                    print("eeeea vamos a jugar, dale")
                    cambiar_dificultad = input("¿Quieres cambiar la dificultad? (si/no): ").lower()
                    if cambiar_dificultad == "si":
                        min_num, max_num = dificultad()
                        print("¡Dificultad cambiada!")
                    else:
                        print("seguimos con la misma dificultad")     
                    # Reiniciar el juego
                    random_number = random.randint(min_num, max_num)
                    intentos = 0
        elif intento > random_number:
                print(f"te pasaste rey, el número es menor que {intento}")
        else:   
                print(f"te falta rey, el número es mayor que {intento}")

def main():
    print("qué haces pa, este es mi primer mini proyecto")
    juego()
   



if __name__ == "__main__":
    main()
