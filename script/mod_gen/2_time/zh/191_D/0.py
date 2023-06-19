def main():
    x,y,r = input().split(' ')
    x = float(x)
    y = float(y)
    r = float(r)
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                count += 1
    print(count)

if __name__ == '__main__':
    main()