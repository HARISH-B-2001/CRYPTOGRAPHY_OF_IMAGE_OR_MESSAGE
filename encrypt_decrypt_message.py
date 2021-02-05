import Fernet
def key():
    key = Fernet.generate_key()
    return key

def encryption(text,key):
    encoded_message = text.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decryption(encrypted_message,key):
    f = Fernet(key)
    decrypted_message = (f.decrypt(encrypted_message)).decode()
    return decrypted_message

if __name__ == '__main__':
    a=str(input())
    c=key()
    b=encryption(a,c)
    print(decryption(b,c))
