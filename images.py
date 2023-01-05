import numpy as np
import cv2
from scipy.interpolate import interp1d
from math import floor


def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]


def image_to_ascii(img, scale_percent: int):

    arr = np.array(img)[:, :, 0]

    # record the original shape
    shape = arr.shape

    # get dimensions for rescaling
    width = int(shape[1] * scale_percent / 100)
    height = int(shape[0] * scale_percent / 100)
    dim = (width, height)

    res = cv2.resize(arr, dsize=dim, interpolation=cv2.INTER_CUBIC)

    # crop to centre
    dif = (width - height) // 2
    res = res[:, dif:-dif]

    # make a 1-dimensional view of arr
    flat_arr = res.ravel()

    # lum characters
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.                                "

    # map norm. array values to index of chars
    m = interp1d([0, flat_arr.max()], [len(chars) - 1, 0])

    # get array of lum characters
    ascii_arr = [chars[floor(m(x))] for x in flat_arr]

    # reshape back into 2D array
    return np.asarray(ascii_arr).astype(object).reshape(res.shape)


if __name__ == '__main__':
    img = cv2.imread('./2.jpg')

    ascii_arr = image_to_ascii(img, 5)

    with open('./ascii_new.txt', 'w') as f:
        for line in ascii_arr:
            f.write(' '.join(line))
            f.write('\n')



