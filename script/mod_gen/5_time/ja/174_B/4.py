def main():
    n,d = map(int,input().split())
    x = []
    y = []
    for i in range(0,n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    cnt = 0
    for i in range(0,n):
        if x[i]**2 + y[i]**2 <= d**2:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()