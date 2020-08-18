#!/usr/bin/env python
from PIL import Image


def Decrypt():
    alphabet = {
        (60, 60, 60): 'a', (61, 60, 60): 'b', (60, 61, 60): 'c', (60, 60, 61): 'd', (61, 61, 60): 'e',
        (60, 61, 61): 'f', (61, 60, 61): 'g', (61, 61, 61): 'h', (62, 61, 61): 'i', (61, 62, 61): 'j',
        (61, 61, 62): 'k', (62, 62, 61): 'l', (62, 61, 62): 'm', (61, 62, 62): 'n', (62, 62, 62): 'o',
        (63, 62, 62): 'p', (62, 63, 62): 'q', (62, 62, 63): 'r', (63, 63, 62): 's', (63, 62, 63): 't',
        (62, 63, 63): 'u', (63, 63, 63): 'v', (64, 63, 63): 'w', (63, 64, 63): 'x', (63, 63, 64): 'y',
        (64, 64, 64): 'z', (65, 64, 64): '\'', (65, 65, 64): ',', (65, 65, 65): '.', (61, 62, 63): ' ',
        (63, 62, 61): '>', (62, 63, 61): '!', (61, 63, 62): '?'
    }
    im = Image.open("Encrypted_Image1.png")
    pix = im.load()
    msg = ''
    flag = True

    st_pixel = [1, 935]
    while flag:
        pix_val = pix[st_pixel[0], st_pixel[1]]
        letter = alphabet[pix_val]
        if letter == ">":
            file = open("Message.txt", "w")
            file.write(msg)
            file.close()

        msg += letter
        st_pixel[0] += 1
        if st_pixel[1] % 778 == 1:
            st_pixel[1] += 1
            st_pixel[0] = 0


print(Decrypt())
