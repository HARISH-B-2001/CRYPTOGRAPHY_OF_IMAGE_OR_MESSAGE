from cryptography.fernet import Fernet                              #import cryptography module
def key():                                                          #generate key
    key = Fernet.generate_key()
    return key

def encryption(text,key):                                           
    encoded_message = text.encode()                                #encode the message
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)                 #encrypting the message
    return encrypted_message

def decryption(encrypted_message,key):
    f = Fernet(key)
    decrypted_message = (f.decrypt(encrypted_message)).decode()    #decrypting and decode the message
    return decrypted_message

if __name__ == '__main__':
    a=str(input())
    c=key()
    b=encryption(a,c)
    print(decryption(b,c))
