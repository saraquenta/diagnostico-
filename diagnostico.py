def programa_interactivo():
    print("--- BIENVENIDO AL DESAFÍO DEL COFRE DE CALÍOPE ---")
    
    while True:
        try:
            print("\nIntroduce los valores para la prueba:")
            n = int(input("Cantidad de días (N): "))
            k = int(input("Número mágico del calendario (K): "))

            suma_total = (n * (n + 1)) // 2
            
            print(f"La suma total de monedas en {n} días es: {suma_total}")

            if suma_total % k == 0:
                print("RESULTADO: ¡SI! El cofre se ha abierto y revela el mapa.")
            else:
                print("RESULTADO: NO. El cofre permanece cerrado.")

            continuar = input("\n¿Quieres probar con otros números? (s/n): ").lower()
            if continuar != 's':
                print("¡Mucha suerte en tu aventura, Calíope!")
                break
                
        except ValueError:
            print("Error: Por favor, ingresa solo números enteros.")

programa_interactivo()