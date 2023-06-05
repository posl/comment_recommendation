def problem180_d():
    x,y,a,b = map(int,input().split())
    i = 0
    while True:
        if x*a < x+b and x*a < y:
            x = x*a
            i += 1
        else:
            break
    i += (y-x-1)//b
    print(i)

if __name__ == '__main__':
    problem180_d()