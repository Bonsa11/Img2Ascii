import numpy as np
import cv2
from scipy.interpolate import interp1d
from math import floor
import pygame
from images import image_to_ascii


def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]


if __name__ == '__main__':

    screen_width = 1000
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("ASCII Webcam")
    Font = pygame.font.SysFont('timesnewroman', 10)

    white = (255, 255, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 255)
    orange = (255, 100, 0)
    black = (0,0,0)
    done = False

    clock = pygame.time.Clock()
    FPS = 60

    # define a video capture object
    vid = cv2.VideoCapture(0)

    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.                                "


    while (True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        ascii = image_to_ascii(frame)

        pygame.image.save(ascii, 'frame.png')
        

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
