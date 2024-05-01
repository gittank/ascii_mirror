import cv2
import numpy as np
import curses
from curses import wrapper


def main():
    # replace each pixel with a character from array
    chars = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','\\','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','!','l','I',';',':',',','"','^','`','\'','.',' ']

    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    #chars.reverse()

    cap = cv2.VideoCapture(0)
    sc = curses.initscr()
    h, w = sc.getmaxyx()
    curses.noecho()

    while(True):
        ret, frame = cap.read()
        # print(h,w)
        # print(frame.shape)
        # break
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame = np.sum(frame, axis=2)
        frame = (frame // 3)


        fh,fw = frame.shape
        step_h = fh // (h-1)
        step_w = fw // (w-1)
            
        den = 255
        if den == 0:
            gain = 1
        else:
            gain =(len(chars)-1) / den

        frame = frame * gain
        frame = frame - np.min(np.ravel(frame))


        frame = frame.astype('int')
        frame = frame[0::step_h, 0::step_w]
        frame = frame[:h, :w-1]
 
        ascii_image = np.zeros_like(frame).astype('unicode')
        for val in np.unique(frame):
            ascii_image[frame==val] = chars[val]

        for ii,row in enumerate(ascii_image):
            sc.addstr(ii, 0, ''.join(row))
        sc.refresh()

    cap.release()
    cv2.destroyAllWindows()


    # plt.imshow(frame)
    # plt.show()

wrapper(main())
