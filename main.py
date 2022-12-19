import random
options = ("piedra", "papel", "tijera")
round = 1
user_point = 0
computer_points = 0
print("Bienvenido al juego de piedra, papel o tijera")
while True:
    print("-" * 20)
    print("Ronda ", round)
    print("-" * 20)
    user_option = input("piedra, papel o tijera? =>")
    user_option = user_option.lower()
    if user_option not in options:
        print("Opcion no valida")
        continue

    computer_option = random.choice(options)
    print("User option : ", user_option)
    print("Computer option : ", computer_option)

    if user_option == computer_option:
        print("Empate")
        print("User : ", user_point)
        print("Computer : ", computer_points)


    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("User gano !!")
            user_point += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

        else:
            print("papel gana a piedra")
            print("Computer gano !!")
            computer_points += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("User gano !!")
            user_point += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

        else:
            print("tijera gana a papel")
            print("Computer gano !!")
            computer_points += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("User gano !!")
            user_point += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

        else:
            print("piedra gana a tijera")
            print("Computer gano !!")
            computer_points += 1
            print("User : ", user_point)
            print("Computer : ", computer_points)

    round += 1

    if user_point == 3:

        print("User gano el juego")
        print(f"🎖️ El ganador es el usuario con {user_point} puntos 🎖️")
        break

    elif computer_points == 3:

        print("Computer gano el juego")
        print(f"🎖️ El ganador es el Computer con {computer_points} puntos 🎖️\n")
        break
    
    