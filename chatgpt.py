import tkinter
import openai
from tkinter import END

app = tkinter.Tk()
app.title("ChatGPT Bot")
app.geometry("600x600")
app.config(bg = "#000000")
app.iconbitmap("ai_lt.ico")


# openai stuff

openai.api_key = "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"


# function
def speak():

    chat_question = chat_entery.get()

    # create a chat completion
    chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": f"{chat_question}"}])

    # print the chat completion
    chat_text.insert(END, f"\n\nMe: {chat_question}")
    chat_text.insert(END, f"\n\nChatBot: {chat_response.choices[0].message.content}")

    # reset chat entery
    chat_entery.delete(0, END)


def clear_chat():
    chat_text.delete(1.0, END)

# Layout

# chat_frame
chat_frame = tkinter.Frame(app)
chat_frame.pack(pady=20)

# text area
chat_text = tkinter.Text(chat_frame, bg="#343638", width=65, bd=1, fg="#d6d6d6", relief="flat")
chat_text.grid(row=0, column=0)

# scrolbar
text_scrolbar = tkinter.Scrollbar(chat_frame, command=chat_text.yview)
text_scrolbar.grid(row=0, column=1, sticky="ns")
chat_text.config(yscrollcommand=text_scrolbar.set)

# Enter for asking the chatBot
chat_entery = tkinter.Entry(app, borderwidth=1, width=80)
chat_entery.pack(pady=10, padx=20, ipady=20)

# Create Buttons Frame
button_frame = tkinter.Frame(app, bg="#000000")
button_frame.pack(pady=15)

# speak button
speak_button = tkinter.Button(button_frame, text="Speak to ChatGPT", command=speak)
speak_button.grid(row=0, column=0, padx=25)

# clear button
clear_button = tkinter.Button(button_frame, text="Clear Chat", command=clear_chat)
clear_button.grid(row=0, column=1, padx=35)

app.mainloop()