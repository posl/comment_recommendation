def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    max = 10**9
    min = -10**9
    while max - min > 1:
        x = (max + min) // 2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while r - l > 1:
                    c = (l + r) // 2
                    if A[c] * A[i] < x:
                        r = c
                    else:
                        l = c
                count += N - r
            else:
                l = -1
                r = N
                while r - l > 1:
                    c = (l + r) // 2
                    if A[c] * A[i] < x:
                        l = c
                    else:
                        r = c
                count += r
            if A[i] * A[i] < x:
                count -= 1
        count //= 2
        if count < K:
            min = x
        else:
            max = x
    print(max)

if __name__ == '__main__':
    solve()