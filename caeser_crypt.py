import caeser_cipher
import random

choice = input("Press 'E' to encrypt or 'D' to decrypt: ").lower()

file_path_input = input("Enter the INPUT file path: ")

file_path_output = input("Enter the OUTPUT file path: ")

if choice == 'e':
    try:
        shift = random.randint(0,256)
        input_data = open(file_path_input)
        output_data = open(file_path_output,'w',encoding='utf-8')
        input_message = input_data.read()
        
        output_message = caeser_cipher.encrypt(input_message,shift)
        
        output_data.write(output_message)
        output_data.close()
        input_data.close()
        print(f"Encrypted with shift {shift}.")
        input()
    
    except:
        print("Error")

elif choice == 'd':
    try:
        shift = int(input("Enter the amount to be shifted"))
        
        input_data = open(file_path_input,encoding='utf-8')
        output_data = open(file_path_output,'w',encoding='utf-8')
        input_message = input_data.read()
        output_message = caeser_cipher.decrypter(input_message,shift)
        output_data.write(output_message)
        output_data.close()
        input_data.close()
        print("Decryption complete.")

    except:
        print("Error")




