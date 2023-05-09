def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    for i in range(q):
        l, r = 0, 10**18
        while r - l > 1:
            mid = (l + r) // 2
            if sum(mid // ai for ai in a) >= k[i]:
                r = mid
            else:
                l = mid
        print(r)
