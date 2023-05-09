def main():
    import sys
    import math
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        count = 0
        for a in A:
            if a>>i&1:
                count += 1
        ans += (1<<i) * count * (N-count)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()