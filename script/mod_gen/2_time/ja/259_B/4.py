def main():
    a,b,d = map(int,input().split())
    #print(a,b,d)
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    print(x,y)
    return

if __name__ == '__main__':
    main()