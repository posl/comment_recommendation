def main():
    a,b,d = map(int, input().split())
    import math
    d = math.radians(d)
    a,b = a*math.cos(d) - b*math.sin(d), a*math.sin(d) + b*math.cos(d)
    print(a,b)

if __name__ == '__main__':
    main()