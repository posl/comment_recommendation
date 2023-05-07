def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        for i in range(60):
            if a >> i & 1:
                d[i] += 1
    ans = 0
    for i in range(60):
        ans += ((N - d[i]) * d[i] * pow(2, i, 10 ** 9 + 7)) % (10 ** 9 + 7)
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()