print("Decrypt string using the Cipher Wheel method")

string = input("Enter string: ")
letters = list(string)

encrypted = "efghijklmnopqrstuvwxyzabcd "
encrypted = list(encrypted)
alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabet = list(alphabet)

decrypted_letters = []

for letter in letters:
    get_index = encrypted.index(letter)
    fetch_letter = alphabet[get_index]
    decrypted_letters.append(fetch_letter)


decrypted_string = ''.join(decrypted_letters)

print(decrypted_string)
