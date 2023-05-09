def main():
    import math
    import sys
    input = sys.stdin.readline
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r,x+r+1):
        if (r**2-(x-i)**2)**0.5%1 == 0:
            ans += 1
    for i in range(y-r,y+r+1):
        if (r**2-(y-i)**2)**0.5%1 == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()