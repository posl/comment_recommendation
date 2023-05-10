def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.insert(0, 0)
    A.append(10**19)
    for i in range(1, N+1):
        A[i] -= i
    for i in range(Q):
        k = K[i]
        l = 0
        r = N+1
        while r - l > 1:
            m = (l + r) // 2
            if A[m] < k:
                l = m
            else:
                r = m
        print(k + l)

if __name__ == '__main__':
    main()