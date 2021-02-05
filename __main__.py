import PySimpleGUI as sg
import encrypt_decrypt_image as cry_ig
import encrypt_decrypt_message as cry_me

choice=[]

en_key=[]
encoded_text=[]
decoded_text=[]

layout0=[
    [sg.Text("Choose encryption or decryption of Message/Image"),sg.Combo(['Message','Image'],key='type'),sg.Button(button_text='OK'),
     sg.Button(button_text='Exit')]
        ]

layout1 = [
    [sg.Text("Choose 'e' for encryption / 'd' for decryption "),sg.Combo(['e','d'],key='type')],
    [sg.Text('Enter the PATH of the image:'),sg.InputText("", key='adress')],
    [sg.Text('Enter the key(0-255):'),sg.InputText("", key='code'),sg.Button(button_text='OK'),sg.Button(button_text='Exit')],
         ]

layout1a=[
    [sg.Text("Congratulation! Your image is encrypted as enc.py")],
    [sg.Button(button_text='OK')]
        ]

layout1b=[
    [sg.Text("Congratulation! Your image is decrypted as dec.py")],
    [sg.Button(button_text='OK')]
        ]

layout2 =layout2 =[
    [sg.Text('ENCRYPTION', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Enter the message:  '),sg.InputText("", key='text'),sg.Button(button_text='Encrypt'),sg.Button(button_text='Exit')],
    [sg.Text('Key:                        '),sg.InputText("",key='key_c')],
    [sg.Text('Encrypted Message:'),sg.InputText("",key="en_text_c")],
    [sg.Text('DECRYPTION', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Enter the Key:                       '),sg.InputText("", key='key_r')],
    [sg.Text('Enter the Encrypted Message:'),sg.InputText("", key='en_text_r'),sg.Button(button_text='Decrypt')],
    [sg.Text('Encrypted Message:'),sg.InputText("", key="de_text")]
                  ]



window0 = sg.Window('Crytography', layout0)
event0, values0 = window0.Read()
if event0=='OK':
    choice.append(values0['type'])
elif event0 in (None, 'Exit'):
    window0.Close()
window0.Close()

if choice[0]=='Image':
    window1 = sg.Window('Crytography', layout1)
    while True:
        event1, values1 = window1.Read()
        if event1 == 'OK':
            if values1['type'] == 'e':
                cry_ig.encrypt(values1['adress'], values1['code'])
                window1a = sg.Window('Crytography', layout1a)
                event1a = window1a.Read()
                if event1a in (None, 'OK'):
                    window1a.Close()
                break
            elif values1['type'] == 'd':
                cry_ig.decrypt(values1['adress'], values1['code'])
                window1b = sg.Window('Crytography', layout1b)
                event1b = window1b.Read()
                if event1b in (None, 'OK'):
                    window1b.Close()
                break
        elif event1 in (None, 'Exit'):
            break

    window1.Close()



elif choice[0]=='Message':
    window2 = sg.Window('Crytography', layout2)
    while True:
        event2, value2 = window2.Read()
        if event2 == 'Encrypt':
            en_key.append(cry_me.key())
            encoded_text.append(cry_me.encryption(value2['text'], en_key[0]))
            window2.FindElement('key_c').Update(en_key[0])
            window2.FindElement('en_text_c').Update(encoded_text[0])

        elif event2 == 'Decrypt':
            en_message = value2['en_text_r']
            key = value2['key_r']
            decoded_text.append(cry_me.decryption(en_message.encode(), key.encode()))
            window2.FindElement('de_text').Update(decoded_text[0])



        elif event2 in (None, 'Exit'):
            break

    window2.Close()
