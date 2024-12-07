import tkinter as tk
import random
from ctypes import windll, c_long

def handle_yes():
    message_label.config(text="ХА-ХА! Я знала, что ты признаешься!")
    app_window.after(3000, app_window.destroy)

def move_no_button_randomly(event):
    new_x = random.randint(0, app_window.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, app_window.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x, y=new_y)

def relocate_window():
    screen_width = app_window.winfo_screenwidth()
    screen_height = app_window.winfo_screenheight()
    random_x = random.randint(0, screen_width - app_window.winfo_width())
    random_y = random.randint(0, screen_height - app_window.winfo_height())
    app_window.geometry(f"+{random_x}+{random_y}")

def check_cursor_near_close_button():
    hwnd = windll.user32.GetForegroundWindow()
    rect = (c_long * 4)()
    windll.user32.GetWindowRect(hwnd, rect)
    x1, y1, x2, y2 = rect
    close_button_x_start = x2 - 50
    close_button_y_start = y1
    close_button_x_end = x2
    close_button_y_end = y1 + 30
    cursor_pos = (c_long * 2)()
    windll.user32.GetCursorPos(cursor_pos)
    cursor_x, cursor_y = cursor_pos
    if close_button_x_start <= cursor_x <= close_button_x_end and close_button_y_start <= cursor_y <= close_button_y_end:
        relocate_window()

def block_window_closing():
    relocate_window()

app_window = tk.Tk()
app_window.title("Детектор лжи")
app_window.geometry("500x300")
app_window.config(bg="#2E2E2E")

app_window.protocol("WM_DELETE_WINDOW", block_window_closing)

main_font = ("Verdana", 16, "bold")
button_font = ("Verdana", 12, "bold")
background_color = "#2E2E2E"
text_color = "#F5F5F5"
button_color = "#FF5722"
hover_button_color = "#E64A19"

message_label = tk.Label(app_window, text="СОСАЛ??)0)", font=main_font, bg=background_color, fg=text_color)
message_label.pack(pady=20)

button_style = {
    "font": button_font,
    "width": 10,
    "height": 2,
    "bg": button_color,
    "fg": text_color,
    "activebackground": hover_button_color,
    "activeforeground": "#FFFFFF",
    "bd": 0,
    "highlightthickness": 0
}

yes_button = tk.Button(app_window, text="Да", command=handle_yes, **button_style)
yes_button.place(x=70, y=180)

no_button = tk.Button(app_window, text="Нет", **button_style)
no_button.place(x=310, y=180)

no_button.bind("<Enter>", move_no_button_randomly)

def monitor_close_button():
    check_cursor_near_close_button()
    app_window.after(100, monitor_close_button)

monitor_close_button()

app_window.mainloop()
