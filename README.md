run in Python interpreter or call from another program
import stego
stego.hide("infilename.ext", "Text to hide", "outfilename.ext")
stego.unhide("imagewithhiddendata.ext")

3 pixels per byte. Standard bytes are 0x00 to 0xFF. A "byte" of 0x100 acts as an end sentinel. 

I like bitwise math. It wasn't written to be easily comprehended. 

I had a free 45 minutes and a challenge. 
