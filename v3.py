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

while key_pressed != chr(27):   
    initial_time = time.time()
    
    key_pressed = sys.stdin.read(1)[0]
    
    print(key_pressed.upper(), end="", flush=True)
    
    try:
        key = str(last_key_pressed.upper() + key_pressed.upper())
        value = time.time() - initial_time
        
        if key in data:
            data[key].append(value)
        else:
            data[key] = [value]
        
    except KeyError as ke:
        print(type(ke), format(ke))
            
    
    initial_time = 0
    last_key_pressed = key_pressed
    
print(data)

with open('data.txt', 'w') as arq:
    arq.write(str(data))

# for key,secret in data:
#     print('Combination:', key, '\t', 'Value:', secret)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)




