from matplotlib import pyplot as plt
from pprint import pprint
import numpy as np
import cv2 as cv
import os


files = (
    os.path.join('./images/', x)
    for x in os.listdir('./images/')
    if x.endswith('.png') or x.endswith('.jpg')
)


def black_count(img) -> int:
    rows, cols = img.shape[:2]
    count = 0

    for i in range(rows):
      for j in range(cols):
         rgb = img[i, j]
         
         if all(0 <= x <= 50 for x in rgb):
             count += 1
         else:
             img[i, j] = [255, 255, 255]

    return img, count


counts = {}


for filename in files:
    img = cv.imread(filename)

    # Grayscale-based filtering:
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # ret, img = cv.threshold(img, 50, 255, cv.THRESH_BINARY)

    img, count = black_count(img)
    rows, cols = img.shape[:2]
    pixel_count = rows * cols
    percent = round(count / pixel_count * 100, 2)

    cv.imshow('Output:', img)
    cv.imwrite(f'./outputs/{filename}', img)

    print(filename)
    print('Black-pixel count:', count)
    print('Percentage:', percent)
    counts[filename.split('/')[-1]] = percent

    key = cv.waitKey(5000)#pauses for 3 seconds before fetching next image
    if key == 27:#if ESC is pressed, exit loop
        cv.destroyAllWindows()
        break


pprint(counts)


# plt.plot(list(range(len(counts))), list(counts.values()))
# plt.show()
# plt.savefig('./graph.png')


