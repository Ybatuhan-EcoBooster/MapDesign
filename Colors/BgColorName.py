#For Colors
import webcolors

# Documentation https://webcolors.readthedocs.io/en/latest/contents.html#webcolors.name_to_hex

class ColorConverter:
    '''
    Hex code Should be six digit. 
    Hex = start with # and #123456
    R = Red
    G = Green
    B = Blue
    RGB = (int,int,int)
    '''

    def ColorName(self = None, rGb = None, rgB = None):
        try:
            if rGb is not None:
                RGB_code = webcolors.rgb_to_name([self,rGb,rgB])
                bgcolor_name = RGB_code 
        
            else:
                try:
                    Hex_code = webcolors.hex_to_name(self)
                    bgcolor_name = Hex_code
                except:
                    print("!!! Hex Code Length Should Be # + 6 digit -- Such as #000000  !!!")
        except:
            print("Please try !!!  --- Such as #FFFFFFFF or (255,0,0) or [255,0,0]")

        return bgcolor_name

    def RGBHex(self = None,rGb = None, rgB = None):
        try:
            if rGb is not None:
                rgbtohex = webcolors.rgb_to_hex([self,rGb,rgB])
            else:
                r = self[0]
                g = self[1]
                b = self[2]
                rgbtohex = webcolors.rgb_to_hex([r,g,b])
        except:
            print("Please try !!!  --- Such as  RGBHex(255,0,0) or RGBHex([255,0,0]) or RGBHex((255,0,0))")

        return rgbtohex
