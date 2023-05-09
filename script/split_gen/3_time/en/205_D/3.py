def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A
    A.append(10**18)
    for k in K:
        l = 0
        r = N + 1
        while r - l > 1:
            m = (r + l) // 2
            if A[m] - (m + 1) < k:
                l = m
            else:
                r = m
        print(l + k)
