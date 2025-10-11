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
# BTN_BG 和 BTN_ACTIVE 保持不變

# 通用樣式
style.configure('TFrame', background=BG_MAIN)
style.configure('Card.TFrame', background=BG_CARD, relief='flat', borderwidth=0)
style.configure('TLabel', background=BG_CARD, foreground=FG_TEXT, font=('Segoe UI', 11))
style.configure('Header.TLabel', font=('Segoe UI Semibold', 12, 'bold'), foreground='#F5F5F5', background=BG_CARD)

# 🚀 修正 1: 確保 Status.TLabel 字體足夠且一致
style.configure('Status.TLabel', font=('Consolas', 11, 'bold'), background=BG_CARD)

# 按鈕樣式保持不變
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
ttk.Button(initFrame, text='Load Entities', command=handler.initButtonClick, width=18).pack(anchor='center', pady=10)

ttk.Separator(initFrame, orient='horizontal').pack(fill='x', pady=15)

# **修正 Init 區塊排版 (使用 grid 解決文字切邊)**
mini_map_frame = ttk.Frame(initFrame, style='Card.TFrame')
mini_map_frame.pack(fill='x', pady=(5, 5), padx=5) # 增加父框架的水平內部間距

# 設定兩欄排版
mini_map_frame.grid_columnconfigure(0, weight=1)  # 讓 Mini Map Position: 佔用剩餘空間
mini_map_frame.grid_columnconfigure(1, weight=0)  # 狀態標籤不需要拉伸

# 標題 (左對齊)
ttk.Label(mini_map_frame, text='Mini Map Position:', foreground=FG_SUB, background=BG_CARD).grid(row=0, column=0, sticky='w')

# 狀態 (右對齊)
# 🚀 修正 2: 保持 miniStatusLabel 與 Status.TLabel 樣式一致
miniStatusLabel = ttk.Label(mini_map_frame, text='Waiting', foreground='#F0AE13', style='Status.TLabel')
miniStatusLabel.grid(row=0, column=1, sticky='e')


# --- Live Info 區塊 ---
ttk.Label(liveFrame, text='📡 Live Info', style='Header.TLabel').pack(anchor='center', pady=(0, 20))

# Live Info 區塊排版 (使用 grid 確保間距和對齊)
coordinate_frame = ttk.Frame(liveFrame, style='Card.TFrame')
coordinate_frame.pack(fill='x', pady=(5, 5), padx=5) # 增加父框架的水平內部間距

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

# 🚀 修正 3: 使用 pack 且不使用硬編碼 padx，讓間距更自然
ttk.Label(status_frame, text='Status:', foreground=FG_SUB, background=BG_CARD).pack(side='left')
botStatusLabel = ttk.Label(status_frame, text='not running', foreground=ERROR, style='Status.TLabel')
botStatusLabel.pack(side='left') # 移除 padx=10，讓字體自然間隔


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

    # Normalize status and set the state
    if status is True or (isinstance(status, str) and status.lower() == 'done'):
        # 確保 'Done' 的文字不會被切邊，且顏色正確
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