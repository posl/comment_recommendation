def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    l, r = 0, 10**9
    while r-l > 1:
        m = (l+r)//2
        if check(A, K, m):
            r = m
        else:
            l = m
    print(r)

if __name__ == '__main__':
    main()