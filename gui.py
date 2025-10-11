import tkinter as tk
from tkinter import ttk
import handler

# 初始化主視窗
root = tk.Tk()
root.geometry('520x580')
root.title('🐾 Puppy Controller')
root.config(background='#1E1E1E')
root.resizable(False, False)

# --- 樣式設定 ---
style = ttk.Style()
style.theme_use('clam')

# 主題配色
BG_MAIN = '#1E1E1E'
BG_CARD = '#1E1E1E'
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'
BORDER = '#2B2B2B'
BTN_BG = '#2F2F2F'
BTN_ACTIVE = '#3D3D3D'

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='solid', borderwidth=1)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)
style.configure('TButton',
                background=BTN_BG,
                foreground='#FFFFFF',
                font=('Segoe UI', 11, 'bold'),
                padding=(8, 8),
                borderwidth=0)
style.map('TButton',
          background=[('active', BTN_ACTIVE)],
          foreground=[('active', '#FFFFFF')])

style.configure('Running.TButton',
                background=ACCENT,
                foreground='#FFFFFF',
                font=('Segoe UI', 11, 'bold'))
style.map('Running.TButton',
          background=[('active', '#14D542')],
          foreground=[('active', '#FFFFFF')])

# --- 主框架 ---
main_frame = ttk.Frame(root, padding=25, style='TFrame')
main_frame.pack(expand=True, fill='both')

# --- 子卡片區塊 ---
initFrame = ttk.Frame(main_frame, padding=20, style='Card.TFrame')
liveFrame = ttk.Frame(main_frame, padding=20, style='Card.TFrame')
optionsFrame = ttk.Frame(main_frame, padding=25, style='Card.TFrame')

# 網格排版
initFrame.grid(row=0, column=0, padx=(0, 15), pady=(0, 15), sticky="nsew")
liveFrame.grid(row=0, column=1, padx=(15, 0), pady=(0, 15), sticky="nsew")
optionsFrame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="ew")

main_frame.grid_columnconfigure(0, weight=1, uniform='a')
main_frame.grid_columnconfigure(1, weight=1, uniform='a')
main_frame.grid_rowconfigure(0, weight=1)

# --- Init 區塊 ---
ttk.Label(initFrame, text='⚙️ Init', style='Header.TLabel').pack(anchor='center', pady=(0, 20))
ttk.Button(initFrame, text='Load Entities', command=handler.initButtonClick, width=18).pack(anchor='center', pady=10)

ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

ttk.Label(initFrame, text='Mini Map Position:', foreground=FG_SUB, background=BG_CARD).pack(anchor='w', pady=(5, 5))
miniMapLabel = ttk.Label(initFrame, text='Waiting', foreground='#F0AE13', background=BG_CARD, font=('Consolas', 10))
miniMapLabel.pack(anchor='e')

# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

ttk.Label(liveFrame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).pack(anchor='w', pady=(5, 5))
coordinatesLabel = ttk.Label(liveFrame, text='(10,10)', font=('Consolas', 10), background=BG_CARD)
coordinatesLabel.pack(anchor='e')

# --- 控制區 ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)
ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left', padx=10)

# --- 更新函式 ---
def updateMiniMapLabel(error=None):
    if error is not None:
        miniMapLabel['foreground'] = ERROR
        miniMapLabel['text'] = error
    else:
        miniMapLabel['text'] = 'Done'
        miniMapLabel['foreground'] = ACCENT

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

# --- 主迴圈 ---
root.mainloop()
