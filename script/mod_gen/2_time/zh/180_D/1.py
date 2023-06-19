def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while x*a <= x+b and x*a < y:
        x *= a
        exp += 1
    print(exp + (y-x-1)//b)

if __name__ == '__main__':
    main()