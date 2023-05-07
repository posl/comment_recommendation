def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = A[-1] + 1
    while r - l > 1:
        mid = (l + r) // 2
        if check(A, mid, K):
            l = mid
        else:
            r = mid
    print(l)
