def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.append(10**18)
    for k in K:
        l, r = 0, 10**18
        while r - l > 1:
            m = (l + r) // 2
            cnt = 0
            for i in range(N + 1):
                if A[i] <= m:
                    cnt += m - A[i] + 1
                else:
                    break
            if cnt >= k:
                r = m
            else:
                l = m
        print(r)

if __name__ == '__main__':
    main()