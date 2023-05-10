def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    for i in range(Q):
        x = X[i]
        l = 0
        r = N - 1
        while r - l > 1:
            m = (l + r) // 2
            if A[m] >= x:
                r = m
            else:
                l = m
        if A[l] >= x:
            print(N - l)
        elif A[r] >= x:
            print(N - r)
        else:
            print(0)

if __name__ == '__main__':
    main()