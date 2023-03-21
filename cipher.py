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

if __name__ == '__main__':
    # Get the message and shift from the user
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message using the Caesar Cipher
    encrypted_message = caesar_cipher(message, shift)
    
    # Print the encrypted message
    print("Encrypted message:", encrypted_message)
