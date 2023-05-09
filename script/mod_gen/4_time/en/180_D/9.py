def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while(True):
        if (a*x >= x+b) and (a*x < y):
            x = a*x
            exp += 1
        else:
            break
    print(exp + (y-1-x)//b)

if __name__ == '__main__':
    main()