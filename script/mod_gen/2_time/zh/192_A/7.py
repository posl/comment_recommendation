def main():
    x,y,r = map(float, input().split())
    x,y,r = int(x*10000), int(y*10000), int(r*10000)
    x1 = int((x-r)/10000)
    x2 = int((x+r)/10000)
    cnt = 0
    for i in range(x1, x2+1):
        y1 = int((r**2 - (i*10000-x)**2)**0.5/10000)
        y2 = int(-(r**2 - (i*10000-x)**2)**0.5/10000)
        cnt += y1 - y2 + 1
    print(cnt)

if __name__ == '__main__':
    main()