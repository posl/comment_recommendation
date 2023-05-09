def main():
    x,y,r = map(float,input().split())
    #print(x,y,r)
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    #print(x,y,r)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if i**2 + j**2 <= r**2:
                count += 1
    print(count)

if __name__ == '__main__':
    main()