def rotate(a,b,d):
    import math
    d = math.radians(d)
    import numpy as np
    x = np.array([[math.cos(d),-math.sin(d)],[math.sin(d),math.cos(d)]])
    y = np.array([a,b])
    z = np.dot(x,y)
    return z
print(rotate(-505,191,278))
