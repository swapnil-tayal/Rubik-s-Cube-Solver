import cv2 as cv
import color_detect


def default(blank):


    cv.putText(blank, 'UPPER', (30, 50), cv.FONT_ITALIC, 1, (255, 255, 255), 1)
    cv.putText(blank, 'FRONT', (30, 350), cv.FONT_ITALIC, 1, (255, 0, 0), 1)
    cv.putText(blank, 'RIGHT', (30, 640), cv.FONT_ITALIC, 1, (0, 0, 255), 1)
    cv.putText(blank, 'DOWN', (330, 50), cv.FONT_ITALIC, 1, (0, 255, 255), 1)
    cv.putText(blank, 'BACK', (330, 350), cv.FONT_ITALIC, 1, (0, 255, 0), 1)
    cv.putText(blank, 'LEFT', (330, 640), cv.FONT_ITALIC, 1, (0, 140, 255), 1)


    #(side == 'upper'):

    # cv.rectangle(blank, (30, 50), (270, 290), (255, 255, 255), thickness=cv.FILLED)


    cv.rectangle(blank, (30, 50), (110, 130), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 50), (190, 130), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 50), (270, 130), (255, 255, 255), thickness=cv.FILLED)

    cv.rectangle(blank, (30, 130), (110, 210), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 130), (190, 210), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 130), (270, 210), (255, 255, 255), thickness=cv.FILLED)

    cv.rectangle(blank, (30, 210), (110, 290), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 210), (190, 290), (255, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 210), (270, 290), (255, 255, 255), thickness=cv.FILLED)

    cv.line(blank, (30, 50), (270, 50), (0, 0, 0), 3)
    cv.line(blank, (30, 130), (270, 130), (0, 0, 0), 3)
    cv.line(blank, (30, 210), (270, 210), (0, 0, 0), 3)
    cv.line(blank, (30, 290), (270, 290), (0, 0, 0), 3)
    
    cv.line(blank, (30, 50), (30, 290), (0, 0, 0), 3)
    cv.line(blank, (110, 50), (110, 290), (0, 0, 0), 3)
    cv.line(blank, (190, 50), (190, 290), (0, 0, 0), 3)
    cv.line(blank, (270, 50), (270, 290), (0, 0, 0), 3)

    #(side == 'front'):

    # cv.rectangle(blank, (30, 350), (270, 590), (255, 255, 255), thickness=cv.FILLED)

    cv.rectangle(blank, (30, 350), (110, 430), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 350), (190, 430), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 350), (270, 430), (255, 0, 0), thickness=cv.FILLED)
    
    cv.rectangle(blank, (30, 430), (110, 510), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 430), (190, 510), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 430), (270, 510), (255, 0, 0), thickness=cv.FILLED)
    
    cv.rectangle(blank, (30, 510), (110, 590), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 510), (190, 590), (255, 0, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 510), (270, 590), (255, 0, 0), thickness=cv.FILLED)

    cv.line(blank, (30, 350), (270, 350), (0, 0, 0), 3)
    cv.line(blank, (30, 430), (270, 430), (0, 0, 0), 3)
    cv.line(blank, (30, 510), (270, 510), (0, 0, 0), 3)
    cv.line(blank, (30, 590), (270, 590), (0, 0, 0), 3)

    cv.line(blank, (30, 350), (30, 590), (0, 0, 0), 3)
    cv.line(blank, (110, 350), (110, 590), (0, 0, 0), 3)
    cv.line(blank, (190, 350), (190, 590), (0, 0, 0), 3)
    cv.line(blank, (270, 350), (270, 590), (0, 0, 0), 3)


    # (side == 'right'):

    # cv.rectangle(blank, (30, 640), (270, 880), (255, 255, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (30, 640), (110, 720), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 640), (190, 720), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 640), (270, 720), (0, 0, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (30, 720), (110, 800), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 720), (190, 800), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 720), (270, 800), (0, 0, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (30, 800), (110, 880), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (110, 800), (190, 880), (0, 0, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (190, 800), (270, 880), (0, 0, 255), thickness=cv.FILLED)

    cv.line(blank, (30, 640), (270, 640), (0, 0, 0), 3)
    cv.line(blank, (30, 720), (270, 720), (0, 0, 0), 3)
    cv.line(blank, (30, 800), (270, 800), (0, 0, 0), 3)
    cv.line(blank, (30, 880), (270, 880), (0, 0, 0), 3)

    cv.line(blank, (30, 640), (30, 880), (0, 0, 0), 3)
    cv.line(blank, (110, 640), (110, 880), (0, 0, 0), 3)
    cv.line(blank, (190, 640), (190, 880), (0, 0, 0), 3)
    cv.line(blank, (270, 640), (270, 880), (0, 0, 0), 3)

    # (side == 'down'):

    # cv.rectangle(blank, (330, 50), (570, 290), (0, 0, 0), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 50), (410, 130), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 50), (490, 130), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (470, 50), (570, 130), (0, 255, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 130), (410, 210), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 130), (490, 210), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (470, 130), (570, 210), (0, 255, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 210), (410, 290), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 210), (490, 290), (0, 255, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (470, 210), (570, 290), (0, 255, 255), thickness=cv.FILLED)

    cv.line(blank, (330, 50), (570, 50), (0, 0, 0), 3)
    cv.line(blank, (330, 130), (570, 130), (0, 0, 0), 3)
    cv.line(blank, (330, 210), (570, 210), (0, 0, 0), 3)
    cv.line(blank, (330, 290), (570, 290), (0, 0, 0), 3)

    cv.line(blank, (330, 50), (330, 290), (0, 0, 0), 3)
    cv.line(blank, (410, 50), (410, 290), (0, 0, 0), 3)
    cv.line(blank, (490, 50), (490, 290), (0, 0, 0), 3)
    cv.line(blank, (570, 50), (570, 290), (0, 0, 0), 3)


    # (side == 'back'):

    # cv.rectangle(blank, (330, 350), (570, 590), (255, 255, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 350), (410, 430), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 350), (490, 430), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 350), (570, 430), (0, 255, 0), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 430), (410, 510), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 430), (490, 510), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 430), (570, 510), (0, 255, 0), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 510), (410, 590), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 510), (490, 590), (0, 255, 0), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 510), (570, 590), (0, 255, 0), thickness=cv.FILLED)

    cv.line(blank, (330, 350), (570, 350), (0, 0, 0), 3)
    cv.line(blank, (330, 430), (570, 430), (0, 0, 0), 3)
    cv.line(blank, (330, 510), (570, 510), (0, 0, 0), 3)
    cv.line(blank, (330, 590), (570, 590), (0, 0, 0), 3)

    cv.line(blank, (330, 350), (330, 590), (0, 0, 0), 3)
    cv.line(blank, (410, 350), (410, 590), (0, 0, 0), 3)
    cv.line(blank, (490, 350), (490, 590), (0, 0, 0), 3)
    cv.line(blank, (570, 350), (570, 590), (0, 0, 0), 3)


    #(side == 'left'):

    # cv.rectangle(blank, (330, 640), (570, 880), (255, 255, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 640), (410, 720), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 640), (490, 720), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 640), (570, 720), (0, 140, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 720), (410, 800), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 720), (490, 800), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 720), (570, 800), (0, 140, 255), thickness=cv.FILLED)
    
    cv.rectangle(blank, (330, 800), (410, 880), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (410, 800), (490, 880), (0, 140, 255), thickness=cv.FILLED)
    cv.rectangle(blank, (490, 800), (570, 880), (0, 140, 255), thickness=cv.FILLED)

    cv.line(blank, (330, 640), (570, 640), (0, 0, 0), 3)
    cv.line(blank, (330, 720), (570, 720), (0, 0, 0), 3)
    cv.line(blank, (330, 800), (570, 800), (0, 0, 0), 3)
    cv.line(blank, (330, 880), (570, 880), (0, 0, 0), 3)

    cv.line(blank, (330, 640), (330, 880), (0, 0, 0), 3)
    cv.line(blank, (410, 640), (410, 880), (0, 0, 0), 3)
    cv.line(blank, (490, 640), (490, 880), (0, 0, 0), 3)
    cv.line(blank, (570, 640), (570, 880), (0, 0, 0), 3)



def CurrToMyCubePrev(curr, side, blank):


    # converting red to -> (0, 0, 255) this form
    top_left_color = color_detect.fun2(curr[0])
    top_middle_color = color_detect.fun2(curr[1])
    top_right_color = color_detect.fun2(curr[2]) 
    middle_left_color = color_detect.fun2(curr[3]) 
    middle_middle_color = color_detect.fun2(curr[4])  
    middle_right_color = color_detect.fun2(curr[5]) 
    bottom_left_color = color_detect.fun2(curr[6]) 
    bottom_middle_color = color_detect.fun2(curr[7]) 
    bottom_right_color = color_detect.fun2(curr[8]) 

    if(side == 'upper'):

        # cv.rectangle(blank, (30, 50), (270, 290), (255, 255, 255), thickness=cv.FILLED)

        cv.rectangle(blank, (30, 50), (110, 130), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 50), (190, 130), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 50), (270, 130), top_right_color, thickness=cv.FILLED)

        cv.rectangle(blank, (30, 130), (110, 210), middle_left_color, thickness=cv.FILLED)
        # by default upper will be always white
        cv.rectangle(blank, (110, 130), (190, 210), (255, 255, 255), thickness=cv.FILLED)
        cv.rectangle(blank, (190, 130), (270, 210), middle_right_color, thickness=cv.FILLED)

        cv.rectangle(blank, (30, 210), (110, 290), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 210), (190, 290), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 210), (270, 290), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (30, 50), (270, 50), (0, 0, 0), 3)
        cv.line(blank, (30, 130), (270, 130), (0, 0, 0), 3)
        cv.line(blank, (30, 210), (270, 210), (0, 0, 0), 3)
        cv.line(blank, (30, 290), (270, 290), (0, 0, 0), 3)
        
        cv.line(blank, (30, 50), (30, 290), (0, 0, 0), 3)
        cv.line(blank, (110, 50), (110, 290), (0, 0, 0), 3)
        cv.line(blank, (190, 50), (190, 290), (0, 0, 0), 3)
        cv.line(blank, (270, 50), (270, 290), (0, 0, 0), 3)

    if(side == 'front'):

        # cv.rectangle(blank, (30, 350), (270, 590), (255, 255, 255), thickness=cv.FILLED)

        cv.rectangle(blank, (30, 350), (110, 430), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 350), (190, 430), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 350), (270, 430), top_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (30, 430), (110, 510), middle_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 430), (190, 510), (255, 0, 0), thickness=cv.FILLED)
        cv.rectangle(blank, (190, 430), (270, 510), middle_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (30, 510), (110, 590), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 510), (190, 590), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 510), (270, 590), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (30, 350), (270, 350), (0, 0, 0), 3)
        cv.line(blank, (30, 430), (270, 430), (0, 0, 0), 3)
        cv.line(blank, (30, 510), (270, 510), (0, 0, 0), 3)
        cv.line(blank, (30, 590), (270, 590), (0, 0, 0), 3)

        cv.line(blank, (30, 350), (30, 590), (0, 0, 0), 3)
        cv.line(blank, (110, 350), (110, 590), (0, 0, 0), 3)
        cv.line(blank, (190, 350), (190, 590), (0, 0, 0), 3)
        cv.line(blank, (270, 350), (270, 590), (0, 0, 0), 3)


    if(side == 'right'):

        # cv.rectangle(blank, (30, 640), (270, 880), (255, 255, 255), thickness=cv.FILLED)
        
        cv.rectangle(blank, (30, 640), (110, 720), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 640), (190, 720), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 640), (270, 720), top_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (30, 720), (110, 800), middle_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 720), (190, 800), (0, 0, 255), thickness=cv.FILLED)
        cv.rectangle(blank, (190, 720), (270, 800), middle_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (30, 800), (110, 880), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (110, 800), (190, 880), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (190, 800), (270, 880), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (30, 640), (270, 640), (0, 0, 0), 3)
        cv.line(blank, (30, 720), (270, 720), (0, 0, 0), 3)
        cv.line(blank, (30, 800), (270, 800), (0, 0, 0), 3)
        cv.line(blank, (30, 880), (270, 880), (0, 0, 0), 3)

        cv.line(blank, (30, 640), (30, 880), (0, 0, 0), 3)
        cv.line(blank, (110, 640), (110, 880), (0, 0, 0), 3)
        cv.line(blank, (190, 640), (190, 880), (0, 0, 0), 3)
        cv.line(blank, (270, 640), (270, 880), (0, 0, 0), 3)

    if(side == 'down'):

        # cv.rectangle(blank, (330, 50), (570, 290), (0, 0, 0), thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 50), (410, 130), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 50), (490, 130), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 50), (570, 130), top_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 130), (410, 210), middle_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 130), (490, 210), (0, 255, 255), thickness=cv.FILLED)
        cv.rectangle(blank, (490, 130), (570, 210), middle_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 210), (410, 290), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 210), (490, 290), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 210), (570, 290), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (330, 50), (570, 50), (0, 0, 0), 3)
        cv.line(blank, (330, 130), (570, 130), (0, 0, 0), 3)
        cv.line(blank, (330, 210), (570, 210), (0, 0, 0), 3)
        cv.line(blank, (330, 290), (570, 290), (0, 0, 0), 3)

        cv.line(blank, (330, 50), (330, 290), (0, 0, 0), 3)
        cv.line(blank, (410, 50), (410, 290), (0, 0, 0), 3)
        cv.line(blank, (490, 50), (490, 290), (0, 0, 0), 3)
        cv.line(blank, (570, 50), (570, 290), (0, 0, 0), 3)


    if(side == 'back'):

        # cv.rectangle(blank, (330, 350), (570, 590), (255, 255, 255), thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 350), (410, 430), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 350), (490, 430), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 350), (570, 430), top_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 430), (410, 510), middle_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 430), (490, 510), (0, 255, 0), thickness=cv.FILLED)
        cv.rectangle(blank, (490, 430), (570, 510), middle_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 510), (410, 590), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 510), (490, 590), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 510), (570, 590), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (330, 350), (570, 350), (0, 0, 0), 3)
        cv.line(blank, (330, 430), (570, 430), (0, 0, 0), 3)
        cv.line(blank, (330, 510), (570, 510), (0, 0, 0), 3)
        cv.line(blank, (330, 590), (570, 590), (0, 0, 0), 3)

        cv.line(blank, (330, 350), (330, 590), (0, 0, 0), 3)
        cv.line(blank, (410, 350), (410, 590), (0, 0, 0), 3)
        cv.line(blank, (490, 350), (490, 590), (0, 0, 0), 3)
        cv.line(blank, (570, 350), (570, 590), (0, 0, 0), 3)

    
    if(side == 'left'):

        # cv.rectangle(blank, (330, 640), (570, 880), (255, 255, 255), thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 640), (410, 720), top_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 640), (490, 720), top_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 640), (570, 720), top_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 720), (410, 800), middle_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 720), (490, 800), (0, 140, 255), thickness=cv.FILLED)
        cv.rectangle(blank, (490, 720), (570, 800), middle_right_color, thickness=cv.FILLED)
        
        cv.rectangle(blank, (330, 800), (410, 880), bottom_left_color, thickness=cv.FILLED)
        cv.rectangle(blank, (410, 800), (490, 880), bottom_middle_color, thickness=cv.FILLED)
        cv.rectangle(blank, (490, 800), (570, 880), bottom_right_color, thickness=cv.FILLED)

        cv.line(blank, (330, 640), (570, 640), (0, 0, 0), 3)
        cv.line(blank, (330, 720), (570, 720), (0, 0, 0), 3)
        cv.line(blank, (330, 800), (570, 800), (0, 0, 0), 3)
        cv.line(blank, (330, 880), (570, 880), (0, 0, 0), 3)

        cv.line(blank, (330, 640), (330, 880), (0, 0, 0), 3)
        cv.line(blank, (410, 640), (410, 880), (0, 0, 0), 3)
        cv.line(blank, (490, 640), (490, 880), (0, 0, 0), 3)
        cv.line(blank, (570, 640), (570, 880), (0, 0, 0), 3)
        
