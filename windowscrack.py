import random
from pynput import keyboard
from pynput.keyboard import Key, Controller
import os

Dinleyici = None

Kontrolcu = Controller()

Harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J','K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X','Y','Z']
degistirici = False


def basım(tus):
    global Dinleyici, Kontrolcu, Harfler, degistirici
    
    if tus == Key.alt_gr:
        Dinleyici.stop()
        print("Helal Olsun Dayı Oğlu :))")
        
    elif not degistirici:
        
        if hasattr(tus, "char"):
            
            if tus.char in Harfler:
                
                degistirici = True
                Kontrolcu.type("\b")
                item = random.choice(tuple(Harfler))
                Kontrolcu.type(item)
                
                
    elif hasattr(tus, "char"):
        
        if tus.char in Harfler:
            degistirici = False
            
if __name__ == '__main__':
    Dinleyici = keyboard.Listener(on_press=basım)
    Dinleyici.start()
    print("Geçmiş Olsun Dayı Oğlu :))")
    Dinleyici.join()

