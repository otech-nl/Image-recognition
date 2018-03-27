''' this script reads image and label data in to a Pandas data frame and writes it as CSV'''
from PIL import Image
import pandas as pd
import numpy as np


def img2df(path):
    ''' read an image into a dataframe '''
    img = Image.open(path)
    arr = np.array(img.getdata())
    df = pd.DataFrame(arr)
    return df


coords = '163600.0_563400.0'

# read image
img = img2df('./%s.tif' % coords)
img.columns = ['R', 'G', 'B']

# read label and mark water
lbl = img2df('./WaterVlakkenRasterUitBGT_%s.tif' % coords)
lbl['water'] = lbl[0] == 0  # black pixels are water
del lbl[0]

# join image and label
df = img.join(lbl)
width, height = Image.open('./%s.tif' % coords).size
size = width * height
df['x'] = [i % 1000 for i in range(size)]
df['y'] = [i // 1000 for i in range(size)]
df.set_index(['x', 'y'], inplace=True)

df.to_csv('%s.csv' % coords)
print(df)
