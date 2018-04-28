
def encrypt(message,shift):
    '''
    INPUT: The meassage to be encrypted and the amount of shifting to be added.
    required.
    OUTPUT: The encryted version of the message.
    
    Uses only the first 256 characters of the unicode character encoding.

    
    '''
    if shift>255:
        shift -= 255
    encrypt_list=[chr(ord(letter)+shift) for letter in message]
    encrypted_message = ''.join(encrypt_list)

    return encrypted_message
    
    

def decrypter(message,shift):
    '''
    INPUT: Take in the encrypted text and shift
    OUTPUT: The decrypted  message

    Uses only the first 256 characters of the Unicode character encoding.
    '''
    if shift > 255:
        shift -= 255
    decrypt_list = [chr(ord(letter)-shift) for letter in message]
    decrypted_message = ''.join(decrypt_list)

    return decrypted_message






