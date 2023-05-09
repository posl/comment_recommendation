def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while x*a < y and x*a < x+b:
        x *= a
        exp+=1
    exp += (y-x-1)//b
    print(exp)

if __name__ == '__main__':
    main()