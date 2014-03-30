import cv2

def hide(imName, text, outname):
    image = cv2.imread(imName)
    text += chr(0xFF)
    if len(text)*9 > len(image[1,:]) * len(image[:,1]) * 3 - 9:
        print "TEXT TOO LONG"
        return
    for i in range(len(text)):
        for bit in range(9):
            if i == len(text) - 1 or (bit < 8 and ord(text[i]) & 1<<bit):
                image[(i*3 + bit/3)/len(image[1,:]), (i*3 + bit/3)%len(image[1,:]), bit%3] |= 1
            else:
                image[(i*3 + bit/3)/len(image[1,:]), (i*3 + bit/3)%len(image[1,:]), bit%3] &= ~1
    cv2.imwrite(outname, image)
        
def unhide(imName):
    image = cv2.imread(imName)
    text = ""
    for i in range(len(image[1,:]) * len(image[:,1]) ):
        thisByte = 0;
        for bit in range(9):
                thisByte |= (image[(i*3 + bit/3)/len(image[1,:]), (i*3 + bit/3)%len(image[1,:]), bit%3] & 1) << bit
        if thisByte < 256:
            text += chr(thisByte)
        else:
            break
    return text            