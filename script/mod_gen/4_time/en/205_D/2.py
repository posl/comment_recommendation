def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        K = int(input())
        l, r = 0, 10**18
        while r - l > 1:
            m = (l + r) // 2
            if sum(m // a for a in A) < K:
                l = m
            else:
                r = m
        print(r)

if __name__ == '__main__':
    main()