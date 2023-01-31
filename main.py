import cv2 as cv
import numpy as np
import color_detect
import maker
import MYcubePreview
import Info
from kociemba import kociemba

vid = cv.VideoCapture(0)
vid.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

cube = {'up' : ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
        'right': ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'],
        'front': ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'],
        'down': ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
        'left': ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'],
        'back': ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']}


blank = np.zeros((950, 600, 3) , dtype='uint8')
blank2 = np.zeros((230, 1280, 3) , dtype='uint8')

cv.putText(blank2, 'W-upper', (0, 25), cv.FONT_ITALIC , 1, (255, 255, 255))
cv.putText(blank2, 'Z-down', (0, 65), cv.FONT_ITALIC , 1, (0, 255, 255))
cv.putText(blank2, 'A-left', (0, 105), cv.FONT_ITALIC , 1, (0, 140, 255))
cv.putText(blank2, 'D-right', (0, 145), cv.FONT_ITALIC , 1, (0, 0, 255))
cv.putText(blank2, 'F-back', (0, 185), cv.FONT_ITALIC , 1, (0, 255, 0))
cv.putText(blank2, 'S-front', (0, 225), cv.FONT_ITALIC , 1, (255, 0, 0))


cv.putText(blank2, 'Enter-Compute Solution', (400, 30), cv.FONT_ITALIC , 1.2, (255, 255, 255))

MYcubePreview.default(blank)
AnsIndex = -1
text = 'deafult'

while True:

    ret, frame= vid.read()
    frame = cv.flip(frame, 1)
    frame = cv.resize(frame, (1280, 720), fx=0, fy=0, interpolation = cv.INTER_CUBIC)

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    height, width = frame.shape[:2] 
    # print(height, width)

    # Solution(frame)

    tr = [120, 120]
    tm = [360, 120]
    tl = [600, 120]
    mr = [120, 360]
    mm = [360, 360]
    ml = [600, 360]
    br = [120, 600]
    bm = [360, 600]
    bl = [600, 600]


    cv.circle(frame, tr, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, tm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, tl, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, mr, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, mm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, ml, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, br, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, bm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, bl, 15, (255, 255, 255), thickness=cv.FILLED)


    top_left_color = color_detect.fun(hsv_frame[120, 120])
    middle_left_color = color_detect.fun(hsv_frame[360, 120])
    bottom_left_color = color_detect.fun(hsv_frame[600, 120])
    top_middle_color = color_detect.fun(hsv_frame[120, 360])
    middle_middle_color = color_detect.fun(hsv_frame[360, 360])
    bottom_middle_color = color_detect.fun(hsv_frame[600, 360])
    top_right_color = color_detect.fun(hsv_frame[120, 600])
    middle_right_color = color_detect.fun(hsv_frame[360, 600])
    bottom_right_color = color_detect.fun(hsv_frame[600, 600])


    cv.rectangle(frame, (800, 200), (900, 300), color_detect.fun2(top_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 200), (1000, 300), color_detect.fun2(top_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 200), (1100, 300), color_detect.fun2(top_right_color), thickness=cv.FILLED)
    cv.rectangle(frame, (800, 300), (900, 400), color_detect.fun2(middle_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 300), (1000, 400), color_detect.fun2(middle_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 300), (1100, 400), color_detect.fun2(middle_right_color), thickness=cv.FILLED)
    cv.rectangle(frame, (800, 400), (900, 500), color_detect.fun2(bottom_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 400), (1000, 500), color_detect.fun2(bottom_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 400), (1100, 500), color_detect.fun2(bottom_right_color), thickness=cv.FILLED)


    cv.line(frame, (800, 200), (800, 500), (0, 0, 0), 3)
    cv.line(frame, (900, 200), (900, 500), (0, 0, 0), 3)
    cv.line(frame, (1000, 200), (1000, 500), (0, 0, 0), 3)
    cv.line(frame, (1100, 200), (1100, 500), (0, 0, 0), 3)
    
    cv.line(frame, (800, 200), (1100, 200), (0, 0, 0), 3)
    cv.line(frame, (800, 300), (1100, 300), (0, 0, 0), 3)
    cv.line(frame, (800, 400), (1100, 400), (0, 0, 0), 3)
    cv.line(frame, (800, 500), (1100, 500), (0, 0, 0), 3)


    curr = [top_left_color, top_middle_color, top_right_color,
            middle_left_color, middle_middle_color, middle_right_color,
            bottom_left_color, bottom_middle_color, bottom_right_color]

    myCube = ""
    key = cv.waitKey(3) & 0xFF
        

    if(key == ord('w')):
        cube = maker.Curr2Cube(cube, curr, 'upper')
        MYcubePreview.CurrToMyCubePrev(curr, 'upper', blank) 

    if(key == ord('d')):
        cube = maker.Curr2Cube(cube, curr, 'right')
        MYcubePreview.CurrToMyCubePrev(curr, 'right', blank) 

    if(key == ord('s')):
        cube = maker.Curr2Cube(cube, curr, 'front')
        MYcubePreview.CurrToMyCubePrev(curr, 'front', blank) 

    if(key == ord('z')):
        cube = maker.Curr2Cube(cube, curr, 'down')
        MYcubePreview.CurrToMyCubePrev(curr, 'down', blank) 

    if(key == ord('a')):
        cube = maker.Curr2Cube(cube, curr, 'left')
        MYcubePreview.CurrToMyCubePrev(curr, 'left', blank) 

    if(key == ord('f')):
        cube = maker.Curr2Cube(cube, curr, 'back')
        MYcubePreview.CurrToMyCubePrev(curr, 'back', blank) 


    if(key == ord('\r')):
        myCube = maker.cubeToString(cube, myCube)
        print(myCube)
        if(maker.check(myCube) == False):
            print('in valid input')
            text = 'invalid cube'
        else:
            ans = kociemba.solve(myCube)
            text = ans
            ans = ans.split()
            for i in range(len(ans)):
                print(i+1, ans[i])
        

        if(text == 'invalid cube'):
            Info.outputIV(text, blank2)
        else:
            Info.outputAns(text, blank2)
            n = len(ans)
        
    if(key == ord('l')):
        AnsIndex = AnsIndex + 1
        
    if(text != 'invalid cube' and text != 'deafult'):
        Info.output(text, frame, AnsIndex)


    cv.imshow("frame", frame)
    cv.imshow("MyCube", blank)
    cv.imshow("Info", blank2)

    if(key == 27):
        break


vid.release()
cv.destroyAllWindows()
