def rotate(x,y,d):
    return x*math.cos(math.radians(d)) - y*math.sin(math.radians(d)), x*math.sin(math.radians(d)) + y*math.cos(math.radians(d))
import sys
import math
for line in sys.stdin:
    x,y,d = map(float,line.split())
    x,y = rotate(x,y,d)
    print(x,y)
