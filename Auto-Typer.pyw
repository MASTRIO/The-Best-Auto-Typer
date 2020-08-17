# Import
import PySimpleGUI as sg
import time

# Variables
what_to_type = ''

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
        

# Closes Gui and game
window.close()