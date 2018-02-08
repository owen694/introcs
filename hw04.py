# Converts RGB to CMYK
#RGB to CMYK formula
#
#        white = max( red/255, green/255, blue/255)
#        cyan  = (white - red/255) / white
#        magenta = (white - green/255) / white
#        yellow  = (white - blue/255) / white
#       black   = 1 - white

#Test Case:       // indigo
#    ===========================
#    Enter red: 75
#    Enter green: 0
#    Enter blue: 130
#    cyan    = 0.423076923076923
#    magenta = 1.0
#    yellow  = 0.0
#    black   = 0.4901960784313726
#Optional:
#    ---------
#    If all three red, green, and blue values are 0, the resulting color is black (0 0 0 1).

# input 3 integers
red = int(raw_input('enter red: '))
green = int(raw_input ('enter green: '))
blue = int(raw_input ('enter blue: '))

# bound red, green and blue within the range [0,256)
red = red % 256
green = green % 256
blue = blue % 256



#convert to CMYK1
#perform float division
white = max(red/255.0, green/255.0, blue/255.0)
if not (white == 0):
  4


# output
if not ((red == 0)&(green == 0)&(blue == 0)):
    print 'cyan =', cyan
    print 'magenta =', magenta
    print 'yellow =', yellow
    print 'black = ', black
else:
    print 'cyan =', 0
    print 'magenta =', 0
    print 'yellow =', 0
    print 'black = ', 1
