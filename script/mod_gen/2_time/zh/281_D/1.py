def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(k):
        sum += a[i]
    if sum%d == 0:
        print(sum)
        return
    for i in range(k,n):
        sum = sum - a[i-k] + a[i]
        if sum%d == 0:
            print(sum)
            return
    print(-1)

if __name__ == '__main__':
    main()