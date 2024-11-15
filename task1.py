from colorama import Fore, Style, init
import sys

# Initialize colorama for color support on Windows
init(autoreset=True)

# Author and version
__author__ = "G4UR4V007"
__version__ = "1.0"

def display_banner():
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.MAGENTA + Style.BRIGHT + "      Welcome to Caesar Cipher Program      ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.YELLOW + f"Author: {__author__}   Version: {__version__}")
    print(Fore.CYAN + "=" * 40 + "\n" + Style.RESET_ALL)

def caesar_cipher(text, shift, option):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_value = 65 if char.isupper() else 97
            shift_direction = shift if option == "encrypt" else -shift
            result += chr((ord(char) - ascii_value + shift_direction) % 26 + ascii_value)
        else:
            result += char
    return result

def get_user_choice():
    print(Fore.CYAN + "\nCaesar Cipher Options")
    print(Fore.GREEN + "1. Encrypt a message")
    print(Fore.GREEN + "2. Decrypt a message")
    print(Fore.RED + "3. Quit")
    while True:
        choice = input(Fore.YELLOW + "Choose an option (1/2/3): " + Style.RESET_ALL)
        if choice in {"1", "2", "3"}:
            return choice
        print(Fore.RED + "Invalid option. Please enter 1, 2, or 3.")

def get_shift_value():
    while True:
        try:
            shift = int(input(Fore.YELLOW + "Enter a shift value (integer): " + Style.RESET_ALL))
            return shift
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer.")

def main():
    display_banner()

    while True:
        choice = get_user_choice()

        if choice == "1":
            text = input(Fore.YELLOW + "Enter a message to encrypt: " + Style.RESET_ALL)
            shift = get_shift_value()
            encrypted_text = caesar_cipher(text, shift, "encrypt")
            print(Fore.GREEN + "Encrypted text: " + Fore.CYAN + encrypted_text + Style.RESET_ALL)

        elif choice == "2":
            text = input(Fore.YELLOW + "Enter a message to decrypt: " + Style.RESET_ALL)
            shift = get_shift_value()
            decrypted_text = caesar_cipher(text, shift, "decrypt")
            print(Fore.GREEN + "Decrypted text: " + Fore.CYAN + decrypted_text + Style.RESET_ALL)

        elif choice == "3":
            print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
            sys.exit()

# Run the program
main()
