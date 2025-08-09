# Language Translator App
# Developed by Naina Patwa
# CodeAlpha Internship – Task 1
# Built with Python, tkinter, and googletrans

from tkinter import *
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Main window
root = Tk()
root.title("Language Translator Tool")
root.geometry("600x500")
root.config(bg="#F0F4F8")  # light background

translator = Translator()

def translate_text():
    input_text = text_input.get("1.0", END)
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()

    translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
    text_output.delete("1.0", END)
    text_output.insert(END, translated.text)

def speak_output():
    tts = gTTS(text=text_output.get("1.0", END), lang=dest_lang_var.get())
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

# --- Styling ---
label_font = ("Segoe UI", 12, "bold")
button_font = ("Segoe UI", 10, "bold")
button_color = "#1F6FEB"  # blue
button_fg = "white"

# --- Widgets ---
Label(root, text="Enter Text:", font=label_font, bg="#F0F4F8").pack(pady=(10, 0))
text_input = Text(root, height=5, width=60, font=("Segoe UI", 10))
text_input.pack(pady=5)

frame = Frame(root, bg="#F0F4F8")
frame.pack(pady=10)

src_lang_var = StringVar(root)
dest_lang_var = StringVar(root)
src_lang_var.set("en")
dest_lang_var.set("hi")

Label(frame, text="From (code):", font=label_font, bg="#F0F4F8").grid(row=0, column=0, padx=5)
Entry(frame, textvariable=src_lang_var, width=8, font=("Segoe UI", 10)).grid(row=0, column=1, padx=5)

Label(frame, text="To (code):", font=label_font, bg="#F0F4F8").grid(row=0, column=2, padx=5)
Entry(frame, textvariable=dest_lang_var, width=8, font=("Segoe UI", 10)).grid(row=0, column=3, padx=5)

# Buttons
Button(root, text="Translate", command=translate_text, font=button_font,
       bg=button_color, fg=button_fg, width=20).pack(pady=5)

Button(root, text="Speak Output", command=speak_output, font=button_font,
       bg=button_color, fg=button_fg, width=20).pack(pady=5)

# Output
Label(root, text="Translated Text:", font=label_font, bg="#F0F4F8").pack(pady=(15, 0))
text_output = Text(root, height=5, width=60, font=("Segoe UI", 10))
text_output.pack(pady=5)

root.mainloop()
