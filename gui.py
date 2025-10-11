import tkinter as tk
from tkinter import ttk
import itertools

# Import your handler (keep original logic)
import handler

# --- Theme Colors (ChatGPT Dark Mode style) ---
BG_MAIN = "#343541"       # Main background
BG_FRAME = "#444654"      # Frame background
FG_TEXT = "#ECECF1"       # Light text
FG_SUBTEXT = "#A1A1AA"    # Subtext gray
ACCENT_GREEN = "#10A37F"  # ChatGPT green
ACCENT_RED = "#EF4444"    # Red for stop/error
ACCENT_YELLOW = "#FBBF24" # Yellow for waiting

root = tk.Tk()
root.geometry("480x450")
root.title("🐶 Puppy Controller")
root.config(bg=BG_MAIN)
root.resizable(False, False)

# --- Custom ttk style ---
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background=BG_FRAME)
style.configure("TLabel", background=BG_FRAME, foreground=FG_TEXT, font=("Segoe UI", 10))
style.configure("TButton", background=ACCENT_GREEN, foreground="white",
                font=("Segoe UI", 10, "bold"), borderwidth=0, focusthickness=3, focuscolor="none")
style.map("TButton", background=[("active", "#13b58d")], relief=[("pressed", "sunken")])

# --- Frames ---
initFrame = ttk.Frame(root, padding=20)
liveFrame = ttk.Frame(root, padding=20)
bottomFrame = ttk.Frame(root, padding=10)

initFrame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
liveFrame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
bottomFrame.grid(row=2, column=0, columnspan=2, pady=(10, 10))

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# --- Initialize Frame ---
ttk.Label(initFrame, text="Initialize Settings", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

# <<< RESTORED: Load Entities now calls handler.initButtonClick exactly like original >>>
loadButton = tk.Button(
    initFrame,
    text="Load Entities",
    bg=ACCENT_GREEN,
    fg="white",
    activebackground="#13b58d",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=12,
    pady=6,
    borderwidth=0,
    highlightthickness=0,
    command=handler.initButtonClick   # <-- 恢復到原始邏輯
)
loadButton.grid(row=1, column=0, columnspan=2, pady=5)

ttk.Label(initFrame, text="Mini map position:", foreground=FG_SUBTEXT).grid(row=2, column=0, sticky="w", pady=(20, 0))
miniMapLabel = ttk.Label(initFrame, text="Waiting", foreground=ACCENT_YELLOW)
miniMapLabel.grid(row=2, column=1, sticky="e", pady=(20, 0))

# --- Live Frame ---
ttk.Label(liveFrame, text="Live Information", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))
ttk.Label(liveFrame, text="Coordinates:", foreground=FG_SUBTEXT).grid(row=1, column=0, sticky="w")
coordinatesLabel = ttk.Label(liveFrame, text="(10,10)")
coordinatesLabel.grid(row=1, column=1, sticky="e")

# --- Bottom Section ---
startButton = tk.Button(
    bottomFrame,
    text="Start Farming",
    bg=ACCENT_GREEN,
    fg="white",
    activebackground="#13b58d",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=18,
    pady=8,
    borderwidth=0,
    highlightthickness=0,
    command=handler.startButtonClick  # keep original start logic
)
startButton.grid(row=0, column=0, pady=10)

# Hover effect for Start/Stop button
def on_enter(e):
    e.widget.config(bg="#13b58d")
def on_leave(e):
    # reset color based on current state label
    if botStatusLabel["text"] == "running..":
        e.widget.config(bg=ACCENT_RED)
    else:
        e.widget.config(bg=ACCENT_GREEN)

startButton.bind("<Enter>", on_enter)
startButton.bind("<Leave>", on_leave)

ttk.Label(bottomFrame, text="Status:", foreground=FG_SUBTEXT).grid(row=1, column=0, sticky="w", pady=(5, 0))
botStatusLabel = ttk.Label(bottomFrame, text="not running", foreground=ACCENT_RED)
botStatusLabel.grid(row=1, column=0, padx=60, sticky="w")

# --- (Optional) Loading animation (kept but NOT auto-triggered by Load button) ---
loading = False
spinner_cycle = itertools.cycle(["|", "/", "-", "\\"])
spinner_label = ttk.Label(initFrame, text="", foreground=ACCENT_GREEN, font=("Consolas", 14, "bold"))
spinner_label.grid(row=3, column=0, columnspan=2, pady=(20, 0))

def start_loading_animation():
    global loading
    loading = True
    animate_spinner()

def animate_spinner():
    if loading:
        spinner_label.config(text=next(spinner_cycle))
        root.after(100, animate_spinner)

def stop_loading_animation():
    global loading
    loading = False
    spinner_label.config(text="")

# --- Update functions (for handler to call) ---
def updateMiniMapLabel(error=None):
    if error is not None:
        miniMapLabel.config(foreground=ACCENT_RED, text=error)
    else:
        miniMapLabel.config(foreground=ACCENT_GREEN, text="Done")

def updateCurrentCoordinate(point):
    coordinatesLabel.config(text=f"({point.x}, {point.y})")

def updateBotStatus(isRunning):
    if isRunning:
        botStatusLabel.config(text="running..", foreground=ACCENT_GREEN)
        startButton.config(text="Stop Farming", bg=ACCENT_RED, activebackground="#f87171")
    else:
        botStatusLabel.config(text="not running", foreground=ACCENT_RED)
        startButton.config(text="Start Farming", bg=ACCENT_GREEN, activebackground="#13b58d")

# make root palette consistent
root.tk_setPalette(background=BG_MAIN, foreground=FG_TEXT)
root.mainloop()
