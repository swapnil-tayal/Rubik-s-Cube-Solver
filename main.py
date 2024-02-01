import cv2 as cv
import numpy as np
import color_detect
import maker
import MYcubePreview
import Info
from kociemba import kociemba

# vid object to capture frames from the camera and process them in code
vid = cv.VideoCapture(0)
# giving height and widht to vis frame
vid.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

cube = {'up' : ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
        'right': ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'],
        'front': ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'],
        'down': ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
        'left': ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'],
        'back': ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']}


# empty screen for screen1 and screen2
blank = np.zeros((950, 600, 3) , dtype='uint8')
blank2 = np.zeros((230, 1280, 3) , dtype='uint8')

# below screen pannel (screen, text, origin, font, fontsize, color)
cv.putText(blank2, 'W-upper', (0, 25), cv.FONT_ITALIC , 1, (255, 255, 255))
cv.putText(blank2, 'Z-down', (0, 65), cv.FONT_ITALIC , 1, (0, 255, 255))
cv.putText(blank2, 'A-left', (0, 105), cv.FONT_ITALIC , 1, (0, 140, 255))
cv.putText(blank2, 'D-right', (0, 145), cv.FONT_ITALIC , 1, (0, 0, 255))
cv.putText(blank2, 'F-back', (0, 185), cv.FONT_ITALIC , 1, (0, 255, 0))
cv.putText(blank2, 'S-front', (0, 225), cv.FONT_ITALIC , 1, (255, 0, 0))


cv.putText(blank2, 'Enter-Compute Solution', (400, 30), cv.FONT_ITALIC , 1.2, (255, 255, 255))

# side pannel for preview
MYcubePreview.default(blank)
AnsIndex = -1
text = 'deafult'

while True:

    # reads one frame from the video source
    # ret -> boolean variable indicating whether the frame was successfully read
    # frame -> NumPy array representing the image data of the captured frame
    ret, frame= vid.read()

    # horizontal flipping the frame - 1
    frame = cv.flip(frame, 1)

    # -> fx and fy are scaling factors

    # interpolation = cv.INTER_CUBIC -> 
    # Cubic interpolation considers a larger neighborhood of pixels when estimating the 
    # value of a new pixel, resulting in smoother and more visually appealing resized images
    frame = cv.resize(frame, (1280, 720), fx=0, fy=0, interpolation = cv.INTER_CUBIC)

    # HSV (Hue-Saturation-Value) frame from BGR
    # why ? -> for color detection, for easily
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    height, width = frame.shape[:2] 
    # print(height, width)

    # Solution(frame)

    # corrdinates on window, for accessing color
    tr = [120, 120]
    tm = [360, 120]
    tl = [600, 120]
    mr = [120, 360]
    mm = [360, 360]
    ml = [600, 360]
    br = [120, 600]
    bm = [360, 600]
    bl = [600, 600]

    # img center radius color thickness
    cv.circle(frame, tr, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, tm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, tl, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, mr, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, mm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, ml, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, br, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, bm, 15, (255, 255, 255), thickness=cv.FILLED)
    cv.circle(frame, bl, 15, (255, 255, 255), thickness=cv.FILLED)


    # detecting the colors from hsv frame (returns name -> red, blue, white)
    top_left_color = color_detect.fun(hsv_frame[120, 120])
    middle_left_color = color_detect.fun(hsv_frame[360, 120])
    bottom_left_color = color_detect.fun(hsv_frame[600, 120])
    top_middle_color = color_detect.fun(hsv_frame[120, 360])
    middle_middle_color = color_detect.fun(hsv_frame[360, 360])
    bottom_middle_color = color_detect.fun(hsv_frame[600, 360])
    top_right_color = color_detect.fun(hsv_frame[120, 600])
    middle_right_color = color_detect.fun(hsv_frame[360, 600])
    bottom_right_color = color_detect.fun(hsv_frame[600, 600])

    # live detection window for colors
    # img, pt1, pt2, color, thickness           # this represents proper view of colors, like perfect red
    cv.rectangle(frame, (800, 200), (900, 300), color_detect.fun2(top_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 200), (1000, 300), color_detect.fun2(top_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 200), (1100, 300), color_detect.fun2(top_right_color), thickness=cv.FILLED)
    cv.rectangle(frame, (800, 300), (900, 400), color_detect.fun2(middle_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 300), (1000, 400), color_detect.fun2(middle_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 300), (1100, 400), color_detect.fun2(middle_right_color), thickness=cv.FILLED)
    cv.rectangle(frame, (800, 400), (900, 500), color_detect.fun2(bottom_left_color), thickness=cv.FILLED)
    cv.rectangle(frame, (900, 400), (1000, 500), color_detect.fun2(bottom_middle_color), thickness=cv.FILLED)
    cv.rectangle(frame, (1000, 400), (1100, 500), color_detect.fun2(bottom_right_color), thickness=cv.FILLED)

    # white lines for displaying
    cv.line(frame, (800, 200), (800, 500), (0, 0, 0), 3)
    cv.line(frame, (900, 200), (900, 500), (0, 0, 0), 3)
    cv.line(frame, (1000, 200), (1000, 500), (0, 0, 0), 3)
    cv.line(frame, (1100, 200), (1100, 500), (0, 0, 0), 3)
    
    cv.line(frame, (800, 200), (1100, 200), (0, 0, 0), 3)
    cv.line(frame, (800, 300), (1100, 300), (0, 0, 0), 3)
    cv.line(frame, (800, 400), (1100, 400), (0, 0, 0), 3)
    cv.line(frame, (800, 500), (1100, 500), (0, 0, 0), 3)

    # fetching current frame colors, and making cube
    curr = [top_left_color, top_middle_color, top_right_color,
            middle_left_color, middle_middle_color, middle_right_color,
            bottom_left_color, bottom_middle_color, bottom_right_color]

    myCube = ""

    # The & 0xFF operation is applied to extract the least significant 8 bits of the result. 
    # This is often done to ensure compatibility with ASCII values of keyboard keys.

    # waitkey(3) stops the execuation for 3ms and wait for any key event
    # key stores the accsi value
    key = cv.waitKey(3) & 0xFF
        

    # ord() -> gives assci value

    if(key == ord('b')):
        if middle_left_color == "white":
            cube = maker.Curr2Cube(cube, curr, 'upper')
            # blank is right pannel
            MYcubePreview.CurrToMyCubePrev(curr, 'upper', blank) 
        


    if(middle_middle_color == "white"):
        # updates the cube's current side, wrt to key press
        cube = maker.Curr2Cube(cube, curr, 'upper')
        # blank is right pannel
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

    # The carriage return character typically moves the cursor 
    # to the beginning of the line without advancing to the next line.
    if(key == ord('\r')):
        myCube = maker.cubeToString(cube, myCube)
        print(myCube)

        # checking valid cube, like 9 red, 9 blue, 9 white ...
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
            # printing invalid cube on screen
            Info.outputIV(text, blank2)
        else:
            # else printing correct seq of answer
            Info.outputAns(text, blank2)
            n = len(ans)
        
    # on pressing l window shows the next seq in the window
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
