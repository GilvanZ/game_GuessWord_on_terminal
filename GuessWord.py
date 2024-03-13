import random
from time import sleep
import os

def load_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().split()
word_list = load_words('word_list.txt')



def space(times):
    for i in range(times):
        print("")
        
def bye():
    os.system('cls')
    phrase="obrigado por jogar <3"
    for letter in phrase:
        print(letter.upper(),end="", flush=True)
        sleep(0.1)
    sleep(2)
    os.system("cls")
    

def fetch_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "[]"
    return display.strip()

def play_game():
    os.system('cls')
    
    while True:
        word = fetch_random_word()
        guessed_letters = set()
        chance = 5
        run = True
        while run:
            print("[Q][W][E][R][T][Y][U][I][O][P]")
            print("  [A][S][D][F][G][H][J][K][L][Ç]")
            print("    [Z][X][C][V][B][N][M] ")
            space(3)
            print(f"Adivinhe uma palavra com {len(word)} letras")
            space(1)
            print(display_word(word, guessed_letters))
            space(3)
            if chance == 1:
                print("Ultima chance")
            else:
                print("Você tem "+str(chance)+" chances")
            
            guess = input("Tente adivinhar a palavra: ").lower()
            
            if guess == "sair":
                bye()
                return
            if len(guess) != len(word):
                print(f"A palavra deve ter exatamente {len(word)} letras.")
                os.system('cls')
                continue
        
            if guess != word:
                for letter in guess:
                    if letter in word:
                        guessed_letters.add(letter)
            else: guessed_letters.clear()
            
            if guess == word:
                os.system('cls')
                print(f"Parabéns! Você adivinhou a palavra corretamente")
                print("")
                for letter in word:
                    print(" "+ letter.upper(), end="", flush=True)
                    sleep(0.5)
                print("")
                again = input("Quer jogar novamente? (sim/nao): ").lower()
                if again == "nao":
                    bye()
                    break
                elif again == "sim":
                    print("Você tem 5 chances")
                    word = fetch_random_word()
                    print(f"Adivinhe uma palavra com {len(word)} letras:")
                    guessed_letters.clear()
                    chance = 5
                elif again != "sim" or "nao":
                    print("sim / nao")
                        
                    
            chance -= 1
            if chance == 0:
                os.system('cls')
                print(f"Mero perdedor...")
                print("")
                for letter in word:
                    print(" "+ letter.upper(), end="", flush=True)
                    sleep(0.5)
                print("")
                again = input("Quer jogar novamente? (sim/nao): ").lower()
                if again == "sim":
                    print("Você tem 5 chances")
                    word = fetch_random_word()
                    print(f"Adivinhe uma palavra com {len(word)} letras:")
                    guessed_letters.clear()
                    chance = 5
                elif again == "nao":
                    bye()
                    break
            
            print(display_word(word, guessed_letters))  
            os.system('cls')
            
            
        break
            
        
            

play_game()


