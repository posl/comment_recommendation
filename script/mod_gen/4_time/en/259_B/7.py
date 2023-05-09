def main():
    a,b,d = map(int,input().split())
    import math
    d = math.radians(d)
    import numpy as np
    x = np.array([[math.cos(d),-math.sin(d)],[math.sin(d),math.cos(d)]])
    y = np.array([[a],[b]])
    ans = np.dot(x,y)
    print(ans[0][0],ans[1][0])

if __name__ == '__main__':
    main()