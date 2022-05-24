#Caesar Cipher:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position % len(alphabet)]

    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#Ask if keep going the loop
while True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


  print("if you want to restart the cipher program?")
  answer = input()
  if answer.lower() == "no":
    print("Have a nice day")
    break

