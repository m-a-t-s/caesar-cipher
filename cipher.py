# This is a Python implementation of the Caesar Cipher
# The program takes a message and a shift value as input and outputs the encrypted message

def caesar_cipher(message, shift):
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""
    
    # Loop through each letter in the message
    for letter in message:
        # Check if the letter is a lowercase or uppercase letter
        if letter.islower():
            # Convert the letter to a number between 0 and 25
            letter_num = ord(letter) - 97
            # Apply the shift and wrap around if necessary
            new_letter_num = (letter_num + shift) % 26
            # Convert the new number back to a letter and add it to the encrypted message
            new_letter = chr(new_letter_num + 97)
            encrypted_message += new_letter
        elif letter.isupper():
            # Convert the letter to a number between 0 and 25
            letter_num = ord(letter) - 65
            # Apply the shift and wrap around if necessary
            new_letter_num = (letter_num + shift) % 26
            # Convert the new number back to a letter and add it to the encrypted message
            new_letter = chr(new_letter_num + 65)
            encrypted_message += new_letter
        else:
            # If the letter is not a letter (e.g. a space or punctuation), add it to the encrypted message as is
            encrypted_message += letter
    
    return encrypted_message

# Example usage:
# Encrypt the message "HELLO WORLD" with a shift of 3
encrypted_message = caesar_cipher("HELLO WORLD", 3)
print(encrypted_message)  # Output: KHOOR ZRUOG
