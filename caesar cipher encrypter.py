print("Encrypt string using the Cipher Wheel method")

string = input("Enter string: ")
removeSpace = input("Remove spaces? (Y/N)")

if removeSpace == 'Y' or removeSpace == 'y':
    letters = list(string.replace(' ',''))
else:
    letters = list(string)

alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabet = list(alphabet)
encrypted = "efghijklmnopqrstuvwxyzabcd "
encrypted = list(encrypted)

encrypted_letters = []

for letter in letters:
    get_index = alphabet.index(letter)
    fetch_letter = encrypted[get_index]
    encrypted_letters.append(fetch_letter)


encrypted_string = ''.join(encrypted_letters)

print(encrypted_string)
