
# updates the cube's current side, wrt to key press
def Curr2Cube(cube, curr, state):

    if(state == 'upper'):
        for i in range(0, 9):
            cube['up'][i] = curr[i]

    elif(state == 'right'):
        for i in range(0, 9):
            cube['right'][i] = curr[i]

    elif(state == 'front'):
        for i in range(0, 9):
            cube['front'][i] = curr[i]

    elif(state == 'down'):
        for i in range(0, 9):
            cube['down'][i] = curr[i]

    elif(state == 'left'):
        for i in range(0, 9):
            cube['left'][i] = curr[i]

    elif(state == 'back'):
        for i in range(0, 9):
            cube['back'][i] = curr[i]

    return cube

def cubeToString(cube, myCube):

    # proper order according to kociemba
    # up -> right -> front -> down -> left -> black

    for i in range(0, 9):
        # be default detecting it as White color
        if(cube['up'][i] == None):
            myCube += 'W'
        else:
            # else making it, work like kociemba red -> R
            myCube += toSignConv(cube['up'][i])
            
    for i in range(0, 9):
        if(cube['right'][i] == None):
            myCube += 'W'
        else:
            myCube += toSignConv(cube['right'][i])
            
    for i in range(0, 9):
        if(cube['front'][i] == None):
            myCube += 'W'
        else:
            myCube += toSignConv(cube['front'][i])
            
    for i in range(0, 9):
        if(cube['down'][i] == None):
            myCube += 'W'
        else:
            myCube += toSignConv(cube['down'][i])
            
    for i in range(0, 9):
        if(cube['left'][i] == None):
            myCube += 'W'
        else:
            myCube += toSignConv(cube['left'][i])
            
    for i in range(0, 9):
        if(cube['back'][i] == None):
            myCube += 'W'
        else:
            myCube += toSignConv(cube['back'][i])

    return myCube


def toSignConv(color):

    if(color == 'red'):
        return 'R'
    
    elif(color == 'white'):
        return 'U'

    elif(color == 'orange'):
        return 'L'
    
    elif(color == 'blue'):
        return 'F'

    elif(color == 'green'):
        return 'B'
    
    elif(color == 'yellow'):
        return 'D'

def check(myCube):

    # each colors count 9 times
    if(myCube.count('L') != 9):
        return False
    if(myCube.count('U') != 9):
        return False
    if(myCube.count('R') != 9):
        return False
    if(myCube.count('F') != 9):
        return False
    if(myCube.count('B') != 9):
        return False
    if(myCube.count('D') != 9):
        return False

    return True
    