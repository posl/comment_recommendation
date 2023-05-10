def main():
    import sys
    from collections import Counter
    from itertools import product
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    c = [input().strip() for _ in range(H)]
    ans = 0
    for r in range(1 << H):
        for c in range(1 << W):
            cnt = sum(c[i][j] == '#' for i, j in product(range(H), range(W)) if (r >> i) & 1 and (c >> j) & 1)
            if cnt == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()