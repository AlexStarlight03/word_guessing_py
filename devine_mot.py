
import random

def get_word() -> str:
    words = ("python", "programmation", "ordinateur", "developpeur", "algorithme",
             "intelligence", "artificielle", "machine", "apprentissage", "data")
    secret_word = random.choice(words)
    return secret_word

def word_guessing(secret: str, guessed: list, attempts: int, new_word: list) -> list:
    letter = guessed[-1]
    for i in range(len(secret)):
        if secret[i] == letter:
            new_word[i] = letter
    return new_word

def solved(new_word: list, secret: str, attempts: int) -> bool:
    if ''.join(new_word) == secret:
        print(f"Bravo! Tu as deviné le mot secret '{secret}'. Tu as gagné! :)")
        return True
    elif attempts == 0:
        print(f"Tu as perdu! :'(\nLe mot secret était '{secret}'")
    return False

def letter_check(letter: str, letters_guessed: list) -> int:
    if letter == "exit":
        return 1
    elif len(letter) != 1 or not letter.isalpha():
        print("Veuillez entrer une seule lettre.")
        return 2
    elif letter in letters_guessed:
        print("Tu as déjà essayé cette lettre.")
        return 2
    return 0

def word_finding(secret: str) -> bool:
    attempts: int = 8
    letters_guessed: list = list()
    new_word: list = list("_" * len(secret))
    found: bool = False

    while attempts > 0 and not found:
        print("Il te reste", attempts, "essais.")
        print(' '.join(new_word))
        letter = input("Lettre? ")
        check = letter_check(letter, letters_guessed)
        match check:
            case 0:
                pass
            case 1:
                return True
            case 2:
                continue
        letters_guessed.append(letter)
        new_word = word_guessing(secret, letters_guessed, attempts, new_word)
        if letter not in secret:
            attempts -= 1
        found = solved(new_word, secret, attempts)
    return False


# Main function to run the game
def main():
    ending: bool = False
    while not ending:
        print("\nDevine mon mot!\nEssayez de deviner le mot secret.\n")
        secret = get_word()
        ending = word_finding(secret)
        if ending:
            break
        while True:
            play = input("Voulez-vous jouer à nouveau? (oui/non): ").lower()
            if play not in ("oui", "non"):
                print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
                continue
            else:
                break
        if play == "non":
            ending = True
    print("Merci d'avoir joué! :D")
    return


if __name__ == '__main__':
    main()