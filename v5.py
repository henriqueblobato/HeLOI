import numpy as np
import tty
import sys
import termios
import time

orig_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)

data = {}
key_pressed, last_key_pressed = '', ''

while key_pressed != chr(27):   
    initial_time = time.time()
    
    key_pressed = sys.stdin.read(1)[0]
    
    print(key_pressed.upper(), end="", flush=True)
    
    if key_pressed == chr(13): print('\n')
    
    try:
        key = str(last_key_pressed.upper() + key_pressed.upper())
        value = round(time.time() - initial_time, 8)
        
        if value > 3:
            continue
        
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
# for i in a data:
#     print(data[i])

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
