import numpy as np
import cv2
from scipy.interpolate import interp1d
from math import floor

def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]


if __name__ == '__main__':
    img = cv2.imread('./2.jpg')
    arr = np.array(img)[:,:,0]

    # record the original shape
    shape = arr.shape
    #print(shape)
    # (1080, 1920)

    scale_percent = 15  # percent of original size
    width = int(shape[1] * scale_percent / 100)
    height = int(shape[0] * scale_percent / 100)
    dim = (width, height)

    res = cv2.resize(arr, dsize=dim, interpolation=cv2.INTER_CUBIC)

    dif = (width - height) //2
    res = res[:,dif:-dif]

    print(res.shape)

    # make a 1-dimensional view of arr
    flat_arr = res.ravel()
    # print(flat_arr.max())

    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.                                "

    m = interp1d([0, flat_arr.max()], [len(chars)-1, 0])

    ascii_arr = [chars[floor(m(x))] for x in flat_arr]

    arr2 = np.asarray(ascii_arr).astype(object).reshape(res.shape)

    ascii = './ascii_new.txt'

    with open(ascii, 'w') as f:
        for line in arr2:
            f.write(' '.join(line))
            f.write('\n')




