### MISC/Father & Sir

Elder Han noticed his student- Sung Jin Woo's son's academic progress \
showing steady decline and and mailed regarding this to him through google. \
He had discovered a little secret and so Little Woo was very curious and \
managed to intercept their E-mail conversation and got this dump.

Can you figure out what they were discussing?

Author:Azakme#2175

flag : **csoc\{5ir_y0ur_s0N_L0v3s_HACk1n9!}**

#### Writeup

Opening the attachment "Mail" in a Text Editor we find a conversation of 
Elder Han which doesnt make much sense(except being lyrics of a song) and some 
random gibberish letters.
Whats note worthy are lines **Content-Type: image/png** and **Content-Transfer-Encoding: base64** which gives us the idea that the 
gibberish text could be base64 string and that it could actually be an image file.

Using a simple script to convert those texts to bytes and dumping them yield a
valid image (png) and when all the 16 of them are dumped and arranged we obtain the flag.
![Screenshot](source//pics//flag.png)