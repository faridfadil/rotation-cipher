# Rotation Cipher Program
A Python side project that I did in my free time. Currently learning encryption and tkinter in Python and I 
wanted to combine these skills together to make a Rotation Cipher GUI program. Feel free to browse through the code!

## How to download
1. Install Python 3.9.
2. Go to the Code green button at the top right.
3. Download as ZIP.
4. Unzip file and open the rotation_cipher.py file. 

## Logic Overview
The program takes in a shift value from the user and a message to encrypt. The crux of the program lies in the ord() and chr() functions
that are native to Python. A for loop takes the individual characters from the message and converts them into ASCII values. Then, the 
ASCII value is incremented according to the shift value. The new ASCII value is then converted back into a character using the chr() function. 
The new character is then appended to a string using the '+=' operator and is outputted. This logic works with the decoding function in that it just subtracts the
ASCII value instead of adding it. 

## Upsides
The program can take in a very high value for a shift key. You can experiment it yourself but the highest I've gone was around 8,000-10,000.

## Downsides
This method of encryption is susceptible to a brute force decryption method where a loop of range(n) can be used to cycle through all the keys. 

## Program Preview
![image](https://user-images.githubusercontent.com/33313844/117907099-89a86180-b319-11eb-9134-be9aca8901f1.png)

The message "cats are awesome" is encrypted with a shift key of 1105 to yield a coded message "ҴҲӅӄѱҲӃҶѱҲӈҶӄӀҾҶ". 
![image](https://user-images.githubusercontent.com/33313844/117907162-a2b11280-b319-11eb-97ce-572741ddd67c.png)

The coded message "ҴҲӅӄѱҲӃҶѱҲӈҶӄӀҾҶ" is decrypted with the shift key of 1105 to yield the decoded message "cats are awesome"



