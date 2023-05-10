def main():
    import math
    R,X,Y = map(int,input().split())
    distance = math.sqrt(X*X + Y*Y)
    if distance == R:
        print(1)
    elif distance <= 2*R:
        print(2)
    else:
        print(math.ceil(distance/R))

if __name__ == '__main__':
    main()