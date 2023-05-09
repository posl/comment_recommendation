def main():
    a,b,d = map(int,input().split())
    d = d * math.pi / 180
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    print(x,y)

if __name__ == '__main__':
    main()