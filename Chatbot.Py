import tkinter as tk
from tkinter import END

# Rule-based function
def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm a bot, but I'm doing great! How can I assist you?"
    elif "your name" in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    elif "help" in user_input:
        return "Sure! I'm here to help. Ask me anything."
    else:
        return "I'm sorry, I don't understand that. Can you try asking differently?"

# GUI functionality
def send():
    user_msg = entry_box.get()
    if user_msg:
        chat_log.config(state='normal')
        chat_log.insert(END, "You: " + user_msg + "\n")
        response = get_response(user_msg)
        chat_log.insert(END, "Bot: " + response + "\n\n")
        chat_log.config(state='disabled')
        entry_box.delete(0, END)
        chat_log.see(END)

# GUI setup
root = tk.Tk()
root.title("Simple Rule-Based ChatBot")
root.geometry("400x500")

chat_log = tk.Text(root, state='disabled', wrap='word')
chat_log.pack(padx=10, pady=10, fill='both', expand=True)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry_box = tk.Entry(entry_frame, width=30)
entry_box.pack(side=tk.LEFT, padx=(0, 10))
entry_box.bind("<Return>", lambda event: send())

send_button = tk.Button(entry_frame, text="Send", command=send)
send_button.pack(side=tk.RIGHT)

root.mainloop()
