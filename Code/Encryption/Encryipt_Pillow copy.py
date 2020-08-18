#!/usr/bin/env python
from PIL import Image


def Convert_Message_RGB(msg):
    msg = msg.lower()
    msg = list(msg)

    alphabet = {
        'a': (60, 60, 60), 'b': (61, 60, 60), 'c': (60, 61, 60), 'd': (60, 60, 61), 'e': (61, 61, 60),
        'f': (60, 61, 61), 'g': (61, 60, 61), 'h': (61, 61, 61), 'i': (62, 61, 61), 'j': (61, 62, 61),
        'k': (61, 61, 62), 'l': (62, 62, 61), 'm': (62, 61, 62), 'n': (61, 62, 62), 'o': (62, 62, 62),
        'p': (63, 62, 62), 'q': (62, 63, 62), 'r': (62, 62, 63), 's': (63, 63, 62), 't': (63, 62, 63),
        'u': (62, 63, 63), 'v': (63, 63, 63), 'w': (64, 63, 63), 'x': (63, 64, 63), 'y': (63, 63, 64),
        'z': (64, 64, 64), '\'': (65, 64, 64), ',': (65, 65, 64), '.': (65, 65, 65), ' ': (61, 62, 63),
        '>': (63, 62, 61), '!': (62, 63, 61), '?': (61, 63, 62)
    }

    for i in range(len(msg)):
        msg[i] = alphabet[msg[i]]
    return msg


def Encrypt_Image(message):
    im = Image.open("Ben.png")
    pix = im.load()

    st_pixel = [0, 935]
    message = Convert_Message_RGB(message)
    for i in range(len(msg)):
        st_pixel[0] += 1

        if st_pixel[1] % 778 == 1:
            st_pixel[1] += 1
            st_pixel[0] = 0

        pix[st_pixel[0], st_pixel[1]] = message[i]

    im.save("Encrypted_Image1.png")
    file.close()


file = open("Message.txt", "r")
msg = file.read()
Encrypt_Image(msg)
