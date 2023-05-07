def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    maxh = 10**9 + 1
    minh = 0
    while maxh - minh > 1:
        mid = (maxh + minh) // 2
        if check(A, N, K, mid):
            maxh = mid
        else:
            minh = mid
    print(maxh)
