def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        m = (l + r) // 2
        if check(m, A, K):
            r = m
        else:
            l = m
    print(r)
