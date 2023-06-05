def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    n = K//N
    m = K%N
    for i in range(N):
        if a[i] <= n:
            if m > 0:
                print(n+1)
                m -= 1
            else:
                print(n)
        else:
            print(n)

if __name__ == '__main__':
    main()