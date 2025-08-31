import tkinter as tk
import pyttsx3

def speak():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def clear_text():
    text_entry.delete("1.0", tk.END)

# Tkinter Window
root = tk.Tk()
root.title("Text to Speech App")
root.state('zoomed')  # Maximize window automatically
root.config(bg="#AF88EE")


# Heading
heading = tk.Label(root, text="🗣 Text to Speech", font=("Helvetica", 24, "bold"), bg="#AF88EE", fg="#ECF0F1")
heading.pack(pady=20)

# Text Input Box
text_entry = tk.Text(root, height=6, width=45, font=("Helvetica", 14), bg="#622E9E", fg="#ECF0F1", insertbackground="white", relief="flat")
text_entry.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#AF88EE")
btn_frame.pack(pady=15)

speak_btn = tk.Button(btn_frame, text="🔊 Speak", command=speak, bg="#3BA065", fg="white", font=("Helvetica", 14, "bold"), width=12, relief="raised", bd=0, activebackground="#2ECC71")
speak_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="🧹 Clear", command=clear_text, bg="#C0392B", fg="white", font=("Helvetica", 14, "bold"), width=12, relief="raised", bd=0, activebackground="#E74C3C")
clear_btn.grid(row=0, column=1, padx=10)

# Run the window
root.mainloop()
