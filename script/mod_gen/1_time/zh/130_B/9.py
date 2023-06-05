def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    for i in range(n+1):
        if i == 0:
            d = 0
        else:
            d = d + l[i-1]
        if d > x:
            print(i)
            break
        elif d == x:
            print(i+1)
            break
        elif i == n:
            print(i+1)
            break

if __name__ == '__main__':
    main()