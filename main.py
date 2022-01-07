from sense_hat import SenseHat

def Sense_Hat_LED_Matrix():
    #----------------

sense = SenseHat()

e = [209,230,126]
f = [104,222,124]
g = [43,107,76]
h = [0,45,99]

image = [
    h,h,h,h,h,h,h,h,
    h,h,h,f,f,h,h,h,
    h,h,f,g,g,f,h,h,
    h,h,f,e,g,f,h,h,
    h,h,f,g,g,f,h,h,
    h,h,f,g,e,f,h,h,
    h,h,h,f,f,h,h,h,
    h,h,h,h,h,h,h,h,
    ]
sense.set_pixels(image)
