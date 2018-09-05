'''
Created on 30 de mai de 2018

@author: ik
'''

import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)

tty.setraw(sys.stdin)
key_pressed = 0
first_pressed = None
second_pressed = None

while key_pressed != chr(27):
    
    if first_pressed is None:
        first_pressed = sys.stdin.read(1)[0]
    
    key_pressed = sys.stdin.read(1)[0]
    print("\nYou pressed", key_pressed)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) 
