'''
Created on 05 de set de 2018

@author: ik

TODO
    1. Colocar backspace para o usuario apagar as letras
    2. 

Valores de input
    ESC 27
    ENTER 13
'''

import tty
import sys
import termios
import time

orig_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)

data = {}
time_data = []
key_pressed = 0
second_pressed = None
last_key_pressed = ''

while key_pressed != chr(13):
    initial_time = time.time()
    
    key_pressed = sys.stdin.read(1)[0]
    
    print(key_pressed.upper(), end="", flush=True)
    
    try:
        key = str(last_key_pressed.upper() + key_pressed.upper())
        value = time.time() - initial_time
        
        if(len(data[key]) == 0):
            data[key] = [value]
        else:
            old_value = data[key]
            new_value = old_value.append(value)
            data[key] = [new_value]
            
    except Exception as e:
        print(type(e), format(e))
        print('ai pai para')
        sys.exit()
    
    initial_time = 0
    last_key_pressed = key_pressed
    
print(data)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

