"""Morse code player
    Plays back the morse code (not working properly) 
    
    TODO:
      Fix sound, try  https://github.com/Elucidation/MorsePy/blob/master/morse_sound.py
"""

import pygame.mixer
from time import sleep


#This is the problematic part

pygame.mixer.init()
#Making the dits and dahs sounds
dit = pygame.mixer.Sound(".\dit-morse.ogg")
dah = pygame.mixer.Sound(".\dah-morse.ogg")


print(dit.get_length())
print(dah.get_length())
gap = 0.1


def ditSound():
    pygame.mixer.Sound.play(dit)
    sleep(gap)


def dahSound():
    pygame.mixer.Sound.play(dit, loops=2)
    sleep(gap)


def morsesound(morsetext:str)-> None:
    for ch in morsetext:
        if ch == "-":
            dahSound()
            print("-", end="")
        elif ch == ".":
            ditSound()
            print(".", end="")
        else:
            print(" ", end="")
            sleep(gap)

#Testing if everything works correctly

morsesound(".-    -...    -.-.    -..    .    ..-.    --.    ....    ..    .---    -.-    .-..    --    -.    ---    .--.    --.-    .-.    ...    -    ..-    ...-    .--    -..-    -.--    --..    .----    ..---    ...-- ....-    .....    -....    --...    ---..    ----.    -----    .-.-.-    --..--    ..--..    .----.    -.-.--    -..-.    -.--.    -.--.-    .-...    ---...    -.-.-.    -...-    .-.-.    -....-    ..--.- .-..-.    ...-..-    .--.-.")

