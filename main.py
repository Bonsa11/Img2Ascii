# import the opencv library
import cv2
import numpy as np


def nums2chars(arr, chars: str, r: float):
    h = arr.shape[0]
    w = arr.shape[1]
    img = [[''] * w] * h
    for index, c in enumerate(chars):
        min_val = index * r
        max_val = (index + 1) * r
        for y in range(0, h):
            for x in range(0, w):
                if min_val <= arr[y][x] < max_val:
                    img[y][x] = c
    return img


if __name__ == '__main__':

    # define a video capture object
    vid = cv2.VideoCapture(0)

    chars = " .,-~:;=!*#$@"  # 12 luminance indexes

    while (True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        lum = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)[:, :, 0]

        scale_percent = 5  # percent of original size
        width = int(lum.shape[1] * scale_percent / 100)
        height = int(lum.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized = cv2.resize(lum, dim, interpolation=cv2.INTER_AREA)

        r = resized.max() / len(chars)

        # print(resized.shape)
        # (480,640) -> (24,32) @ 5%

        # print(resized[0,0])
        # Display the resulting frame
        # cv2.imshow('frame', resized)

        img = nums2chars(resized, chars, r)

        for i in img:
            print(i)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
