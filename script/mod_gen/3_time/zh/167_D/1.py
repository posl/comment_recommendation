def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(n)]
    b[0] = 1
    now = 1
    for i in range(1,k+1):
        now = a[now-1]
        if b[now-1] == 0:
            b[now-1] = i+1
        else:
            loop = i+1-b[now-1]
            now = 1
            for j in range(k%loop):
                now = a[now-1]
            break
    print(now)

if __name__ == '__main__':
    main()