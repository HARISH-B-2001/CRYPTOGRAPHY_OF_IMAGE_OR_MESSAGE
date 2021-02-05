def encrypt(adress,key):
    fo = open(adress , "rb")
    image = fo.read()
    fo.close()
    image = bytearray(image)
    for index, value in enumerate(image):
        image[index] = value^int(key)
    fo = open("enc.jpg" ,"wb" )
    fo.write(image)
    fo.close()

def decrypt(adress,key):
    fo = open(adress, "rb")
    image = fo.read()
    fo.close()
    image = bytearray(image)
    for index, value in enumerate(image):
        image[index] = value ^int(key)
    fo = open("dec.jpg", "wb")
    fo.write(image)
    fo.close()

if __name__ == '__main__':
    a=input("Enter 'e' for encryption/ 'd' for decryption:")
    adress = input("Enter the adress of the image:")
    key = int(input("Enter the key(0-255):"))
    if a=='e':
        encrypt(adress,key)
    elif a=='d':
        decrypt(adress,key)