import tkinter as tk
from tkinter import ttk
import handler

# Initialize main window
root = tk.Tk()
root.geometry('520x580')
root.title('🐾 Puppy Controller')
root.config(background='#1E1E1E')
root.resizable(False, False)

# --- Style settings ---
style = ttk.Style()
style.theme_use('clam')

# Theme colors
BG_MAIN = '#1E1E1E'
BG_CARD = '#252525'
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'

# Common styles
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)

style.configure('TButton',
                background='#2F2F2F',
                foreground='#FFFFFF',
                font=('Segoe UI', 11, 'bold'),
                padding=(8, 8),
                borderwidth=0)
style.map('TButton',
          background=[('active', '#3D3D3D')],
          foreground=[('active', '#FFFFFF')])

style.configure('Running.TButton',
                background=ACCENT,
                foreground='#FFFFFF',
                font=('Segoe UI', 11, 'bold'))
style.map('Running.TButton',
          background=[('active', '#14D542')],
          foreground=[('active', '#FFFFFF')])

# --- Main frame ---
main_frame = ttk.Frame(root, padding=25, style='TFrame')
main_frame.pack(expand=True, fill='both')

# --- Sub frames ---
initFrame = ttk.Frame(main_frame, padding=20, style='Card.TFrame')
liveFrame = ttk.Frame(main_frame, padding=20, style='Card.TFrame')
optionsFrame = ttk.Frame(main_frame, padding=25, style='Card.TFrame')

# Layout
initFrame.grid(row=0, column=0, padx=(0, 15), pady=(0, 15), sticky="nsew")
liveFrame.grid(row=0, column=1, padx=(15, 0), pady=(0, 15), sticky="nsew")
optionsFrame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="ew")

main_frame.grid_columnconfigure(0, weight=1, uniform='a')
main_frame.grid_columnconfigure(1, weight=1, uniform='a')
main_frame.grid_rowconfigure(0, weight=1)

# --- Init block ---
ttk.Label(initFrame, text='⚙️ Init', style='Header.TLabel').pack(anchor='center', pady=(0, 20))
ttk.Button(initFrame, text='Load Entities', command=handler.initButtonClick, width=18).pack(anchor='center', pady=10)

ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

# --- Live Info block ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5), padx=5)

coordinate_frame.grid_columnconfigure(0, weight=1)
coordinate_frame.grid_columnconfigure(1, weight=0)

ttk.Label(coordinate_frame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).grid(row=0, column=0, sticky='w')

coordinatesLabel = ttk.Label(coordinate_frame, text='(10,10)', style='Status.TLabel', foreground='#00BFFF')
coordinatesLabel.grid(row=0, column=1, sticky='e')

# --- Control block ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)

ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left')

# --- Update functions ---
def updateCurrentCoordinate(point):
    coordinatesLabel['text'] = f'({point.x}, {point.y})'

def updateBotStatus(isRunning):
    if isRunning:
        botStatusLabel['text'] = 'running..'
        botStatusLabel['foreground'] = ACCENT
        startButton['text'] = '⏹ STOP'
        startButton.configure(style='Running.TButton')
    else:
        botStatusLabel['text'] = 'not running'
        botStatusLabel['foreground'] = ERROR
        startButton['text'] = '▶ START'
        startButton.configure(style='TButton')

# --- Main loop ---
root.mainloop()