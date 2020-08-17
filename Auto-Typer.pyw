# Import
import PySimpleGUI as sg
import pynput
from pynput.keyboard import Key, Controller
import time
import keyboard

# Variables
what_to_type = ''

# functions
def simulate_typing():
    keyboard.write(what_to_type, '')
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(1)
    simulate_typing()

# Set Theme
sg.theme('Reddit')

# Main Gui Layout
layout = [  [sg.Text('What would you like to type?')],
            [sg.InputText(do_not_clear=False, tooltip='H E L L O')],
            [sg.Button('Start Typing'), sg.Button('Close Program')]  ]

# Opens Gui
window = sg.Window('The Best Auto Typer', layout)

# Runs when Gui is open
while True:
    event, values = window.read()
    # Runs when CLOSE is pressed
    if event in (sg.WIN_CLOSED, 'Close Program'):
        time.sleep(0.5)
        break
    if event in ('Start Typing'):
        what_to_type = values[0]
        simulate_typing()

# Closes Gui and game
window.close()