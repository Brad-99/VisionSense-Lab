import tkinter as tk
from tkinter import ttk
import handler

# 初始化主視窗
root = tk.Tk()
root.geometry('500x560')
root.title('🐾 Puppy Controller')
root.config(background='#1e1e2e')
root.resizable(False, False)

# --- 樣式設定 ---
style = ttk.Style()
style.theme_use('clam')

# 通用樣式
style.configure('TFrame', background='#1e1e2e')
style.configure('TLabel', background='#1e1e2e', foreground='#ffffff', font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 13, 'bold'), foreground='#f0f0f0')
style.configure('Status.TLabel', font=('Segoe UI Semibold', 11, 'bold'))
style.configure('TButton',
                background='#3b3b4f',
                foreground='#ffffff',
                font=('Segoe UI', 11, 'bold'),
                padding=8,
                borderwidth=0,
                focusthickness=3,
                focuscolor='#454567')
style.map('TButton',
          background=[('active', '#5a5a7a')],
          foreground=[('active', '#ffffff')])

# --- 變數 ---
cbVariable = tk.IntVar()

# --- 主框架 ---
main_frame = ttk.Frame(root, padding=25, style='TFrame')
main_frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- 子區塊 ---
initFrame = ttk.Frame(main_frame, padding=20, style='TFrame')
liveFrame = ttk.Frame(main_frame, padding=20, style='TFrame')
optionsFrame = ttk.Frame(main_frame, padding=25, style='TFrame')

# 使用 grid 排版
initFrame.grid(row=0, column=0, padx=(0, 15), pady=10, sticky="nsew")
liveFrame.grid(row=0, column=1, padx=(15, 0), pady=10, sticky="nsew")
optionsFrame.grid(row=1, column=0, columnspan=2, pady=(25, 10), sticky="ew")

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# --- 初始化區塊 ---
ttk.Label(initFrame, text='⚙️ Initialize Settings', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

ttk.Button(initFrame, text='Load Entities', command=handler.initButtonClick, width=18).pack(anchor='center', pady=10)

ttk.Label(initFrame, text='Mini Map Position:', font=('Segoe UI', 10, 'italic')).pack(anchor='w', pady=(20, 5))
miniMapLabel = ttk.Label(initFrame, text='Waiting', foreground='#f0ae13', font=('Consolas', 10))
miniMapLabel.pack(anchor='e')

# --- 即時資訊區 ---
ttk.Label(liveFrame, text='📡 Live Information', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

ttk.Label(liveFrame, text='Coordinates:', font=('Segoe UI', 10, 'italic')).pack(anchor='w', pady=(20, 5))
coordinatesLabel = ttk.Label(liveFrame, text='(10,10)', font=('Consolas', 10))
coordinatesLabel.pack(anchor='e')

# --- 操作區 ---
startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 15), ipadx=20, ipady=10)

# 用 Frame 包裝狀態顯示
status_frame = ttk.Frame(optionsFrame, style='TFrame')
status_frame.pack(anchor='center', pady=10)

ttk.Label(status_frame, text='Status:', font=('Segoe UI', 11)).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground='#ff5555', style='Status.TLabel')
botStatusLabel.pack(side='left', padx=10)

# --- 函式區 ---
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
        startButton['text'] = '⏹ STOP'
        startButton.configure(style='Running.TButton')
    else:
        botStatusLabel['text'] = 'not running'
        botStatusLabel['foreground'] = '#ff5555'
        startButton['text'] = '▶ START'

# 額外為 Running 狀態設定一個亮色按鈕
style.configure('Running.TButton',
                background='#0aad20',
                foreground='#ffffff',
                font=('Segoe UI', 11, 'bold'))
style.map('Running.TButton',
          background=[('active', '#15d230')],
          foreground=[('active', '#ffffff')])

# --- 啟動主迴圈 ---
root.mainloop()
