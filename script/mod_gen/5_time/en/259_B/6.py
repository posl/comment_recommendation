def main():
    import math
    a,b,d = input().split()
    a = float(a)
    b = float(b)
    d = float(d)
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    print(x,y)

if __name__ == '__main__':
    main()