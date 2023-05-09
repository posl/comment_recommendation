def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    for k in K:
        l, r = 1, 10**18
        while r - l > 1:
            m = (l + r) // 2
            if sum(m // a for a in A) < k:
                l = m
            else:
                r = m
        ans.append(r)
    print('
'.join(map(str, ans)))
