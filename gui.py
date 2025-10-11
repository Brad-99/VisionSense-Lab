import tkinter as tk
from tkinter import ttk
import handler # 假設 handler 模組存在

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
BG_CARD = '#252525'
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)

# 按鈕樣式 (保持不變)
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

# 處理 Load Entities 點擊事件 (現在不再需要更新 minimap 狀態)
def load_entities_command():
    handler.initButtonClick()

ttk.Button(initFrame, text='Load Entities', command=load_entities_command, width=18).pack(anchor='center', pady=10)

# 如果 Init 區塊除了 Load Entities 按鈕外沒有其他元素，
# 可以考慮將分隔線移除或調整排版，但這裡先保留分隔線。
ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

# -------------------------------------------------------------
# 兩排 Minimap 狀態已刪除
# -------------------------------------------------------------


# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

# Live Info 區塊排版 (使用 grid 確保間距和對齊)
coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5), padx=5)

coordinate_frame.grid_columnconfigure(0, weight=1)
coordinate_frame.grid_columnconfigure(1, weight=0)

ttk.Label(coordinate_frame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).grid(row=0, column=0, sticky='w')

# 座標標籤
coordinatesLabel = ttk.Label(coordinate_frame, text='(10,10)', style='Status.TLabel', foreground='#00BFFF')
coordinatesLabel.grid(row=0, column=1, sticky='e')


# --- 控制區 ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

# Status 區塊
status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)

ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left')


# --- 更新函式 ---
# 刪除 updateMiniMapLabel 函式，因為相關 UI 元素已移除

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
root.mainloop()import tkinter as tk
from tkinter import ttk
import handler # 假設 handler 模組存在

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
BG_CARD = '#252525'
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)

# 按鈕樣式 (保持不變)
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

# 處理 Load Entities 點擊事件 (現在不再需要更新 minimap 狀態)
def load_entities_command():
    handler.initButtonClick()

ttk.Button(initFrame, text='Load Entities', command=load_entities_command, width=18).pack(anchor='center', pady=10)

# 如果 Init 區塊除了 Load Entities 按鈕外沒有其他元素，
# 可以考慮將分隔線移除或調整排版，但這裡先保留分隔線。
ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

# -------------------------------------------------------------
# 兩排 Minimap 狀態已刪除
# -------------------------------------------------------------


# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

# Live Info 區塊排版 (使用 grid 確保間距和對齊)
coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5), padx=5)

coordinate_frame.grid_columnconfigure(0, weight=1)
coordinate_frame.grid_columnconfigure(1, weight=0)

ttk.Label(coordinate_frame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).grid(row=0, column=0, sticky='w')

# 座標標籤
coordinatesLabel = ttk.Label(coordinate_frame, text='(10,10)', style='Status.TLabel', foreground='#00BFFF')
coordinatesLabel.grid(row=0, column=1, sticky='e')


# --- 控制區 ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

# Status 區塊
status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)

ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left')


# --- 更新函式 ---
# 刪除 updateMiniMapLabel 函式，因為相關 UI 元素已移除

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
root.mainloop()import tkinter as tk
from tkinter import ttk
import handler # 假設 handler 模組存在

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
BG_CARD = '#252525'
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)

# 按鈕樣式 (保持不變)
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

# 處理 Load Entities 點擊事件 (現在不再需要更新 minimap 狀態)
def load_entities_command():
    handler.initButtonClick()

ttk.Button(initFrame, text='Load Entities', command=load_entities_command, width=18).pack(anchor='center', pady=10)

# 如果 Init 區塊除了 Load Entities 按鈕外沒有其他元素，
# 可以考慮將分隔線移除或調整排版，但這裡先保留分隔線。
ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

# -------------------------------------------------------------
# 兩排 Minimap 狀態已刪除
# -------------------------------------------------------------


# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

# Live Info 區塊排版 (使用 grid 確保間距和對齊)
coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5), padx=5)

coordinate_frame.grid_columnconfigure(0, weight=1)
coordinate_frame.grid_columnconfigure(1, weight=0)

ttk.Label(coordinate_frame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).grid(row=0, column=0, sticky='w')

# 座標標籤
coordinatesLabel = ttk.Label(coordinate_frame, text='(10,10)', style='Status.TLabel', foreground='#00BFFF')
coordinatesLabel.grid(row=0, column=1, sticky='e')


# --- 控制區 ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

# Status 區塊
status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)

ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left')


# --- 更新函式 ---
# 刪除 updateMiniMapLabel 函式，因為相關 UI 元素已移除

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