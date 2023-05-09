def main():
    import sys
    import math
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if tmp > max:
                max = tmp
    print(max)

if __name__ == '__main__':
    main()