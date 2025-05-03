from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    new_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift_amount) % len(alphabet)
            new_text = new_text + alphabet[new_index]
        else:
            new_text += char
    print(f"Here is the {encode_or_decode}d result:\n{new_text}")

print(logo)

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
