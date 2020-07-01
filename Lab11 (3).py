#****
# Name       : Roma Razdan
# Pledge     : I pledge my honor that I have abided by the Stevens Honor System. 
# Motivation : To implement loops in my code. 
#****
from cs5png import PNGImage

def mult(c,n):
    '''Given numbers c & n, return c*n, using only addition and lööps'''
    ans = 0
    for x in range(n):
        ans = ans + c
    return ans

def update(c,n):
    '''Given numbers c & n,
    return z where z(0, c) = z and z(n, c) = z(n-1, c)**2 + c,
    absolutely no recursion'''
    z=0
    for x in range(n):
        z=z**2+c
    return z

def inMSet(c,n):
    '''Given a complex c and a number n, return if the magnitude of z
    never goes above 2 in the process of doing update(...). Don't(!)
    call update'''
    z=0
    for x in range(n):
        if abs(z) <= 2:
            z=z**2+c
        else:
            return False
    return True

def scale(pix, pixelMax, floatMin, floatMax):
    '''Given a pixel value, the max pixel value,
    return where that pixel lies on [floatMin, floatMax] where
    pix=0 -> floatMin and pix=pixelMax -> floatMax'''
    number = (floatMax - floatMin)*(1.0*pix / pixelMax)
    z = floatMin + number
    return z

def mset(n):
    '''Creates a 300x200 image of the Mandelbrot set, where
    the image is of the complex plane with x real [-2, 1] and y imaginary, [-i, i]'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x= scale(col, 300, -2, 1)
            y= scale(row, 200, -1, 1)
            c=x+y*1j
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)
    image.saveFile()

if __name__ == "__main__":
    iterations = 100 # Change this to play with the picture, once everything's working
    mset(iterations)
