def main():
    import sys
    import math
    X, Y, R = map(float, sys.stdin.readline().split())
    #print(X, Y, R)
    #print(type(X), type(Y), type(R))
    X = int(X)
    Y = int(Y)
    R = int(R)
    #print(X, Y, R)
    #print(type(X), type(Y), type(R))
    #print(math.floor(X-R), math.ceil(X+R))
    #print(math.floor(Y-R), math.ceil(Y+R))
    count = 0
    for i in range(math.floor(X-R), math.ceil(X+R)+1):
        for j in range(math.floor(Y-R), math.ceil(Y+R)+1):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                count += 1
    print(count)
