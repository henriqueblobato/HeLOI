'''
Created on 05 de set de 2018

@author: ik

TODO
    1.    Colocar backspace para o usuario apagar as letras
    2.    Colocar keys para ser eixo X
          Colocar keys para ser eixo Y
          Colocar value para ser eixo Z  

Valores de input
    ESC 27
    ENTER 13
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
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


fig = plt.figure()
ax = fig.gca(projection='3d')

X = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7]
Y = [3, 4, 5, 4, 5, 3, 4, 5, 3, 2, 2]
Z = [4, 5, 6, 9, 0, 7, 6, 5, 4, 3, 2]

ax.scatter(X, Y, Z, c='r', marker='o')

