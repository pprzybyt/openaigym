import numpy as np

H = 5
D = 9

A = np.random.randn(10, 6, 3)

def prepro(I):
    """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
    I = I[35:195]  # crop
    I = I[::2, ::2, 0]  # downsample by factor of 2
    I[I == 144] = 0  # erase background (background type 1)
    I[I == 109] = 0  # erase background (background type 2)
    I[I != 0] = 1  # everything else (paddles, ball) just set to 1
    return I.astype(np.float).ravel()

a = []
b = (np.random.randn(6))
c = (np.random.randn(6))
print np.outer(b,c)
print b[c<0]