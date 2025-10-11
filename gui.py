import tkinter as tk

# Import the handler
import handler

root = tk.Tk()

# This is the declaration of the variable associated with the checkbox
cbVariable = tk.IntVar()

# Set black background and white foreground for the whole window
root.geometry('400x400')
root.title('puppy')
root.config(background='#000000')
root.resizable(False, False)

# create all of the main containers
initFrame = tk.Frame(root, width=200, height=200, borderwidth=2, relief="groove", bg='#000000')
liveFrame = tk.Frame(root, width=155, height=200, borderwidth=2, relief="groove", bg='#000000')

# layout all of the main containers
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=1)

initFrame.grid(row=0, column=0, sticky="W", padx=15, pady=15)
liveFrame.grid(row=0, column=1, sticky="E", padx=15, pady=15)

# Init Frame
tk.Label(root, text='Initialize settings', fg='#FFFFFF', bg='#000000', font=('arial', 9, 'bold')) \
    .grid(row=0, column=0, sticky="N", pady=20)
tk.Button(root, text='Load Entities', bg='#222222', fg='#FFFFFF', font=('arial', 9, 'normal'),
          command=handler.initButtonClick).grid(row=0, column=0, sticky="S", pady=40)
tk.Label(root, text='Mini map position:', fg='#FFFFFF', bg='#000000', font=('arial', 9, 'normal')).grid(row=0, column=0, sticky="NW",
                                                                                          padx=25, pady=85)
miniMapLabel = tk.Label(root, text='Waiting', fg='#f0ae13', bg='#000000', font=('arial', 9, 'normal'))
miniMapLabel.grid(row=0, column=0, sticky="NE", padx=35, pady=85)

# Live Frame

tk.Label(root, text='Live information', fg='#FFFFFF', bg='#000000', font=('arial', 9, 'bold')).grid(row=0, column=1, sticky="N",
                                                                                      pady=20)

tk.Label(root, text='Coordinates:', fg='#FFFFFF', bg='#000000', font=('arial', 9, 'normal')).grid(row=0, column=1, sticky="NW",
                                                                                    padx=25, pady=85)
coordinatesLabel = tk.Label(root, text='(10,10)', fg='#FFFFFF', bg='#000000', font=('arial', 9, 'normal'))
coordinatesLabel.grid(row=0, column=1, sticky="NE", padx=35, pady=85)

# Options Frame

# Start Section
startButton = tk.Button(root, text='Start Botting', bg='#222222', fg='#FFFFFF', font=('arial', 12, 'normal'),
                        command=handler.startButtonClick)
startButton.grid(row=4, columnspan=2, sticky="S", pady=10)

tk.Label(root, text='Status:', fg='#FFFFFF', bg='#000000', font=('arial', 10, 'normal')).grid(row=5, column=0, sticky="SW", padx=10)
botStatusLabel = tk.Label(root, text='not running', fg='#FF0000', bg='#000000', font=('arial', 10, 'normal'))
botStatusLabel.grid(row=5, column=0, sticky="SW", padx=55)


def updateMiniMapLabel(error=None):
    if error is not None:
        miniMapLabel['fg'] = '#c70c0c'
        miniMapLabel['text'] = error
    else:
        miniMapLabel['text'] = 'Done'
        miniMapLabel['fg'] = '#0aad20'

def updateCurrentCoordinate(point):
    coordinatesLabel['text'] = '({0}, {1})'.format(point.x, point.y)


def updateBotStatus(isRunning):
    if isRunning:
        botStatusLabel['text'] = 'running..'
        botStatusLabel['fg'] = '#0aad20'
        startButton['text'] = 'Stop Farming'
    else:
        botStatusLabel['text'] = 'not running'
        botStatusLabel['fg'] = '#ff0000'
        startButton['text'] = 'Start Farming'