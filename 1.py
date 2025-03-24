import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
from pillow import Image, ImageTk

# Function to handle chatbot responses
#pip install pillow
def chatbot_response(user_message):
    user_message = user_message.lower()

    # Responses based on input message
    if user_message == "hello":
        return "Hi! How can I help?"
    
    elif "price range of" in user_message:
        product = user_message.split("price range of ")[-1]
        return f"The price range for {product} is $50 to $150."
    
    elif "refund" in user_message:
        return "Please contact customer support at +1-800-123-4567."
    
    elif "thank you" in user_message:
        return "You're welcome! Please contact us again."
    
    else:
        return "I'm sorry, I didn't understand that. Could you please clarify?"

# Function to send the message
def send_message():
    user_message = user_input.get()
    if user_message:
        # Display user message in chat
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, f"You: {user_message}\n", "user")
        chatbox.insert(tk.END, f"Bot: {chatbot_response(user_message)}\n\n", "bot")
        chatbox.config(state=tk.DISABLED)
        user_input.set("")
        chatbox.yview(tk.END)

# Create the main window
window = tk.Tk()
window.title("WeChat-Like Chatbot")
window.geometry("400x500")
window.config(bg="lightgray")

# Chatbox for displaying conversation
chatbox = scrolledtext.ScrolledText(window, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20, padx=10, pady=10, bg="white")
chatbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Add tag styles for user and bot messages (colored differently)
chatbox.tag_config("user", foreground="blue", justify="right")
chatbox.tag_config("bot", foreground="green", justify="left")

# Input field for typing messages
user_input = tk.StringVar()
input_entry = tk.Entry(window, textvariable=user_input, width=30, font=("Arial", 12))
input_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Function to load send button image
def load_send_icon():
    img = Image.open("send_icon.png")  # Replace with your send icon image path
    img = img.resize((25, 25), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

# Send button with an icon
send_icon = load_send_icon()
send_button = tk.Button(window, image=send_icon, command=send_message, bg="lightgray", bd=0)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()
