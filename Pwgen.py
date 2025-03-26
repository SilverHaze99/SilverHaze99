import random
import string
#just for examples. Dont use generated passwords for your account
def password_generation(lenght):
    character = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(character) for _ in range(lenght))

def main():
    print("Password-Generator")
    try:
        lenght = int(input("Enter how much characters you need: "))
        print("Your Password:", password_generation(lenght))
    except ValueError:
        print("only numbers!")

if __name__ == "__main__":
    main()
