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
BG_CARD = '#252525' # 將卡片背景色改深一點以增加區隔
FG_TEXT = '#E0E0E0'
FG_SUB = '#AAAAAA'
ACCENT = '#0AAD20'
ERROR = '#C0392B'
BORDER = '#2B2B2B'
BTN_BG = '#2F2F2F'
BTN_ACTIVE = '#3D3D3D'

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
# 將卡片邊框拿掉，讓它看起來更像一個區塊
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)
# Status.TLabel 移除背景色，讓它與其父框架的背景融合
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

# **修正 1：Mini Map Position 區塊排版**
# 創建一個 Frame 來容納 'Mini Map Position:' 和 狀態 Label
mini_map_frame = ttk.Frame(initFrame, style='Card.TFrame')
mini_map_frame.pack(fill='x', pady=(5, 5))

# Title on first line
ttk.Label(mini_map_frame, text='Mini Map:', foreground=FG_SUB, background=BG_CARD).pack(anchor='w')

# Status row on second line: "Waiting | Done" where the active state is highlighted
mini_status_row = ttk.Frame(mini_map_frame, style='Card.TFrame', padding=(0,4))
mini_status_row.pack(fill='x')

# Use grid inside the status row so the status label can align right without being clipped.
mini_status_row.grid_columnconfigure(0, weight=1)
mini_status_row.grid_columnconfigure(1, weight=0)
miniStatusLabel = ttk.Label(mini_status_row, text='Waiting', foreground='#F0AE13', background=BG_CARD, font=('Consolas', 10))
# place on the right with increased vertical padding to avoid clipping
miniStatusLabel.grid(row=0, column=1, sticky='e', padx=(0,6), pady=6)

# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

# **修正 2：Live Info 區塊排版 (與 Mini Map 區塊保持一致)**
# 創建一個 Frame 來容納 'Coordinates:' 和 實際座標 Label
coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5))

ttk.Label(coordinate_frame, text='Coordinates:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
coordinatesLabel = ttk.Label(coordinate_frame, text='(10,10)', font=('Consolas', 10), background=BG_CARD, foreground='#00BFFF')
coordinatesLabel.pack(side='right')


# --- 控制區 ---
ttk.Label(optionsFrame, text='🎮 Controller', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

startButton = ttk.Button(optionsFrame, text='▶ START', command=handler.startButtonClick)
startButton.pack(anchor='center', pady=(5, 20), ipadx=30, ipady=12)

ttk.Separator(optionsFrame, orient='horizontal').pack(fill='x', pady=10)

# **修正 3：移除 botStatusLabel 的「格子」框線**
# Status Label 的父框架 style 還是 Card.TFrame (BG_CARD)
# 確保 botStatusLabel 的背景色與父框架一致，這樣就不會有邊框感
status_frame = ttk.Frame(optionsFrame, style='Card.TFrame')
status_frame.pack(anchor='center', pady=10)
# 將這兩個 Label 的 background 都設為 BG_CARD (optionsFrame/status_frame 的背景色)
ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, background=BG_CARD, style='Status.TLabel')
botStatusLabel.pack(side='left', padx=10)


# --- 更新函式 ---
def updateMiniMapLabel(status=None, error=None):
    """Update the single mini map status label.

    Parameters:
      - status: 'waiting'/'done' or boolean (True -> done, False -> waiting). If omitted, defaults to 'waiting'.
      - error: when provided, shows the error text in red regardless of status.
    """
    if error is not None:
        miniStatusLabel['text'] = str(error)
        miniStatusLabel['foreground'] = ERROR
        return

    # Normalize status
    if status is True or (isinstance(status, str) and status.lower() == 'done'):
        miniStatusLabel['text'] = 'Done'
        miniStatusLabel['foreground'] = ACCENT
    else:
        # default/waiting state
        miniStatusLabel['text'] = 'Waiting'
        miniStatusLabel['foreground'] = '#F0AE13'

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