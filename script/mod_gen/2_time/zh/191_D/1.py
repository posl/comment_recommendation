def problem191_d():
    x,y,r = map(float,input().split())
    x,y,r = int(x*10000),int(y*10000),int(r*10000)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)*(i-x)+(j-y)*(j-y) <= r*r:
                count += 1
    print(count)

if __name__ == '__main__':
    problem191_d()