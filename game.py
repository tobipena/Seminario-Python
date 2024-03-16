import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_failures = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
# Numero de fallos actual
actual_failures = 0
# Cadena de letras vocales
vowels = 'aeiouáéíóú'

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Seleccion de dificultad y aplicando dificultad segun lo definido en el enunciado
print('''Seleccione una de las siguientes dificultades:
        1)Facil
        2)Media
        3)Dificil \n ''')
while True:
    difficult_level = int(input('ingrese el numero correspondiente a la dificultad que quiera: '))
    word_displayed = ''
    match difficult_level:
        case 1:
            for i in secret_word:
                if i in vowels:
                    word_displayed += i
                    guessed_letters.append(i)
                else:
                    word_displayed += '_'
            break
        case 2:
            guessed_letters.append(secret_word[0])
            guessed_letters.append(secret_word[len(secret_word)-1])
            word_displayed = guessed_letters[0] + ('_' * (len(secret_word)-2)) + guessed_letters[1]
            break
        case 3:
            word_displayed = '_' * len(secret_word)
            break
        case _:
            print('valor invalido, intentelo de nuevo')

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while actual_failures < max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada y que la letra no sea un string vacio
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    elif letter == '':
        print('Valor invalido, Intente con otro.')
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        actual_failures += 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_failures} posibles fallos.")
    print(f"La palabra secreta era: {secret_word}")
