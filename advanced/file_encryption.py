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
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


filename = input("Enter the file name: ")
choice = input("Do you want to encrypt or decrypt? ").lower()

shift = 3

try:
    if choice == "encrypt":
        text = read_file(filename)
        encrypted = encrypt(text, shift)

        output_file = "encrypted_" + filename
        write_file(output_file, encrypted)

        print("File encrypted successfully!")
        print("Saved as:", output_file)

    elif choice == "decrypt":
        text = read_file(filename)
        decrypted = decrypt(text, shift)

        output_file = "decrypted_" + filename
        write_file(output_file, decrypted)

        print("File decrypted successfully!")
        print("Saved as:", output_file)

    else:
        print("Invalid choice. Please enter encrypt or decrypt.")

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")