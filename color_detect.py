
def fun (hsv_values):

    h = hsv_values[0]
    s = hsv_values[1]
    v = hsv_values[2]

    if(s > 30):

        if(h < 8):
            return "red"

        elif(h < 20):
            return "orange"

        elif(h < 40):
            return "yellow"

        elif(h < 75):
            return "green"

        elif(h < 132):
            return "blue"
    
    else:
        return "white"


def fun2(color):

    if(color == 'red'):
        return (0, 0, 255)
    
    elif(color == 'orange'):
        return (0, 140, 255)
    
    elif(color == 'yellow'):
        return (0, 255, 255)
    
    elif(color == 'green'):
        return (0, 255, 0)
    
    elif(color == 'blue'):
        return (255, 0, 0)
    
    else:
        return (255, 255, 255)


