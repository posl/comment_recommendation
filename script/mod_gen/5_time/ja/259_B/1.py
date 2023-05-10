def main():
    a,b,d = input().split()
    a = float(a)
    b = float(b)
    d = float(d)
    import math
    d = math.radians(d)
    x = a*math.cos(d) - b*math.sin(d)
    y = a*math.sin(d) + b*math.cos(d)
    print(x,y)

if __name__ == '__main__':
    main()