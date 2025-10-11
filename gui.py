import tkinter as tk
from tkinter import ttk
import handler

# Initialize main window
root = tk.Tk()
root.geometry('450x500')
root.title('🐾Puppy Controller')
root.config(background='#1e1e2e')
root.resizable(False, False)

# Define styles
style = ttk.Style()
style.theme_use('clam')

# Configure custom styles
style.configure('TFrame', background='#1e1e2e')
style.configure('TLabel', background='#1e1e2e', foreground='#ffffff', font=('Arial', 10))
style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
style.configure('Status.TLabel', font=('Arial', 10, 'bold'))
style.configure('TButton', 
                background='#3b3b4f', 
                foreground='#ffffff', 
                font=('Arial', 10),
                padding=10,
                bordercolor='#454567')
style.map('TButton', 
         background=[('active', '#454567')],
         foreground=[('active', '#e0e0e0')])

# Variables
cbVariable = tk.IntVar()

# Create main containers
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create sub-frames
initFrame = ttk.Frame(main_frame, padding=15, relief="flat", style='TFrame')
liveFrame = ttk.Frame(main_frame, padding=15, relief="flat", style='TFrame')
optionsFrame = ttk.Frame(main_frame, padding=15, style='TFrame')

# Layout sub-frames
initFrame.grid(row=0, column=0, padx=(0,10), pady=10, sticky="nsew")
liveFrame.grid(row=0, column=1, padx=(10,0), pady=10, sticky="nsew")
optionsFrame.grid(row=1, column=0, columnspan=2, pady=(20,0), sticky="nsew")

# Init Frame Widgets
ttk.Label(initFrame, text='Initialize Settings', style='Header.TLabel').pack(anchor='n', pady=(0,20))
ttk.Button(initFrame, text='Load Entities', command=handler.initButtonClick).pack(anchor='center', pady=10)
ttk.Label(initFrame, text='Mini Map Position:').pack(anchor='w', pady=(20,5))
miniMapLabel = ttk.Label(initFrame, text='Waiting', foreground='#f0ae13')
miniMapLabel.pack(anchor='e')

# Live Frame Widgets
ttk.Label(liveFrame, text='Live Information', style='Header.TLabel').pack(anchor='n', pady=(0,20))
ttk.Label(liveFrame, text='Coordinates:').pack(anchor='w', pady=(20,5))
coordinatesLabel = ttk.Label(liveFrame, text='(10,10)')
coordinatesLabel.pack(anchor='e')

# Options Frame Widgets
startButton = ttk.Button(optionsFrame, text='Start', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=10)
status_frame = ttk.Frame(optionsFrame)
status_frame.pack(anchor='sw', pady=10)
ttk.Label(status_frame, text='Status:').pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground='#ff0000', style='Status.TLabel')
botStatusLabel.pack(side='left', padx=10)

# Update functions
def updateMiniMapLabel(error=None):
    if error is not None:
        miniMapLabel['foreground'] = '#c70c0c'
        miniMapLabel['text'] = error
    else:
        miniMapLabel['text'] = 'Done'
        miniMapLabel['foreground'] = '#0aad20'

def updateCurrentCoordinate(point):
    coordinatesLabel['text'] = f'({point.x}, {point.y})'

def updateBotStatus(isRunning):
    if isRunning:
        botStatusLabel['text'] = 'running..'
        botStatusLabel['foreground'] = '#0aad20'
        startButton['text'] = 'Stop'
    else:
        botStatusLabel['text'] = 'not running'
        botStatusLabel['foreground'] = '#ff0000'
        startButton['text'] = 'Start'

# Start main loop
root.mainloop()