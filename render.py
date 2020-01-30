import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)

def show(array):
    for i in range(0, 256):
        pixels[i] = array[i]
    
    pixels.show()
