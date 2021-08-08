#ascii encryptor
print("Ignore me :)")

from tkinter import *

#tkinter main window setup
root = Tk()
root.title("Rotation Cipher Program")

#FUNCTIONS
def encode():
        #clear text field
        code_text.delete("1.0", "end-1c")
        #get the shift value from the entry and cast it into an int type
        shift_amount = int(shift_entry.get())
        #get the text entered into the message field
        text = message_entry.get("1.0", "end-1c")
        #empty code string for encoded message to be later appended to. 
        code = ""
        
        #for every letter in the text field
        for letter in text:
                #convert the letter into an ASCII value and add the shift_amount value to it
                encoded_ascii = ord(letter) + shift_amount
                #convert the shifted ASCII value into a character and add it to the empty string
                code += chr(encoded_ascii)
        #print out the value onto the coded message text entry. 
        code_text.insert("1.0", code)
def decode():
        #clear text field
        code_text.delete("1.0", "end-1c")
        #get the shift value from the entry and cast it into an int type
        shift_amount = int(shift_entry.get())
        #get the text entered into the message field
        text = message_entry.get("1.0", "end-1c")
        #empty code string for encoded message to be later appended to. 
        code = ""

        #for every letter in the text field
        for letter in text:
                try:
                        #convert the letter into an ASCII value and subtract the shift_amount value to it
                        decoded_ascii = ord(letter) - shift_amount
                        #convert the shifted ASCII value into a character. 
                        decoded_word = chr(decoded_ascii)
                        #add decoded character to the empty string
                        code += decoded_word
                except:
                        pass
        #print out the value onto the coded message text entry
        code_text.insert("1.0", code)


#TKINTER GUI
shift_label = Label(root, text="Shift Key")
shift_label.grid(row=0, column=0)

shift_entry = Entry(root)
shift_entry.grid(row=0, column=1, sticky=W)

message_label = Label(root, text="Message")
message_label.grid(row=1, column=0, sticky=N)

message_entry = Text(root, height=10, width=50)
message_entry.grid(row=1, column=1)

code_label = Label(root, text="Coded Message")
code_label.grid(row=2, column=0, sticky=N)

code_text = Text(root, height=10, width=50)
code_text.grid(row=2, column=1)

encrypt_button = Button(root, text="Encrypt Message", command=encode)
decrypt_button = Button(root, text="Decrypt Message", command=decode)

encrypt_button.grid(row=3, column=0)
decrypt_button.grid(row=3, column=1, sticky=W)

root.mainloop()


