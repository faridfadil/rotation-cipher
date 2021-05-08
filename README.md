# Rotation Cipher Program
A Python side project that I did in my free time. Currently learning encryption and tkinter in Python and I 
wanted to combine these skills together to make a Rotation Cipher GUI program. Feel free to browse through the code!

## Logic Overview
The program takes in a shift value from the user and a message to encrypt. The crux of the program lies in the ord() and chr() functions
that are native to Python. A for loop takes the individual characters from the message and converts them into ASCII values. Then, the 
ASCII value is then incremented according to the shift value. The new ASCII value is then converted back into a character using the chr() function. 
The new character is then appended to a string using the '+=' operator. This logic works with the decoding function in that it just subtracts the
ASCII value instead of adding it. 

## Upsides
The program can take in a very high value for a shift key. You can experiment it yourself but the highest I've gone was around 8,000-10,000.

## Downsides
This method of encryption is susceptible to a brute force decryption method where a loop of range(n) can be used to cycle through all the keys. 
