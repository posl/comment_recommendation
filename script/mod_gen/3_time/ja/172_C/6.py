def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    time = 0
    cnt = 0
    for i in range(n):
        if time + a[i] <= k:
            time += a[i]
            cnt += 1
        else:
            break
    for i in range(m):
        if time + b[i] <= k:
            time += b[i]
            cnt += 1
        else:
            break
    print(cnt)

if __name__ == '__main__':
    main()