def main():
    a,b,d = map(int,input().split())
    rad = d * 3.141592653589793 / 180
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x,y)

if __name__ == '__main__':
    main()