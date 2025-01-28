import random
import string
#just for examples. Dont use generated passwords for your account
def passwort_generieren(laenge):
    zeichen = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(zeichen) for _ in range(laenge))

def main():
    print("Password-Generator")
    try:
        laenge = int(input("Enter how much characters you need: "))
        print("Your Password:", passwort_generieren(laenge))
    except ValueError:
        print("only numbers!")

if __name__ == "__main__":
    main()
