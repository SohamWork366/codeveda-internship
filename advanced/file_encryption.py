from pathlib import Path


# Always use the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def main():

    print("=== File Encryption / Decryption ===")
    print("Files are located in:", BASE_DIR)
    print()

    filename = input("Enter the file name (example: message.txt): ").strip()
    choice = input("Do you want to encrypt or decrypt? ").strip().lower()

    shift = 3

    # Look for the file inside the same folder as this program
    input_file = BASE_DIR / filename

    # Check if the file exists
    if not input_file.exists():
        print()
        print("File not found.")
        print("Please make sure the file is inside the 'advanced' folder.")
        print()
        print("Available files:")

        files = list(BASE_DIR.iterdir())

        for file in files:
            if file.is_file():
                print(" -", file.name)

        return

    if choice == "encrypt":

        text = read_file(input_file)
        encrypted = encrypt(text, shift)

        output_file = BASE_DIR / ("encrypted_" + input_file.name)

        write_file(output_file, encrypted)

        print()
        print("File encrypted successfully!")
        print("Saved as:", output_file.name)

    elif choice == "decrypt":

        text = read_file(input_file)
        decrypted = decrypt(text, shift)

        output_file = BASE_DIR / ("decrypted_" + input_file.name)

        write_file(output_file, decrypted)

        print()
        print("File decrypted successfully!")
        print("Saved as:", output_file.name)

    else:
        print()
        print("Invalid choice.")
        print("Please enter 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()