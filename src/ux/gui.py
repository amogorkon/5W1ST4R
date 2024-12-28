import tkinter as tk
from tkinter import scrolledtext
from pathlib import Path
from PIL import ImageGrab
from tkhtmlview import HTMLLabel

root = tk.Tk()
root.title("HTML Viewer")
root.geometry("800x600")

html_content = (Path(__file__) / r"../../ui/index.html").read_text()
html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)


def take_screenshot():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = x + root.winfo_width()
    height = y + root.winfo_height()
    ImageGrab.grab().crop((x, y, width, height)).save("screenshot.png")


# Create a frame to hold the chat display and input field
chat_frame = tk.Frame(root)
chat_frame.pack(fill="both", expand=True, pady=10)

# Create a scrollable text widget to display chat messages
chat_display = scrolledtext.ScrolledText(
    chat_frame, wrap=tk.WORD, height=10, state=tk.DISABLED
)
chat_display.pack(fill="both", expand=True)

# Create a frame to hold the input field and the button
input_frame = tk.Frame(chat_frame)
input_frame.pack(fill="x", pady=5)

# Create an entry widget for inputting chat messages
chat_input = tk.Entry(input_frame)
chat_input.pack(side="left", fill="x", expand=True)

# Create a button with three states
mood_states = ["happy", "neutral", "unhappy"]
current_mood = tk.StringVar(value=mood_states[1])  # Default to "neutral"


def cycle_mood():
    current_index = mood_states.index(current_mood.get())
    next_index = (current_index + 1) % len(mood_states)
    current_mood.set(mood_states[next_index])


mood_button = tk.Button(input_frame, textvariable=current_mood, command=cycle_mood)
mood_button.pack(side="right")


def send_message(event=None):
    if message := chat_input.get():
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You ({current_mood.get()}): {message}\n")
        chat_display.config(state=tk.DISABLED)
        chat_input.delete(0, tk.END)


# Bind the Enter key to send the message
chat_input.bind("<Return>", send_message)

root.mainloop()
