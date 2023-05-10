def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    s = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    t = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = float('inf')
        for j in [bisect_left(s, x[i]), bisect_right(s, x[i])]:
            for k in [bisect_left(t, s[j]), bisect_right(t, s[j])]:
                ans = min(ans, abs(x[i] - s[j]) + abs(s[j] - t[k]))
            for k in [bisect_left(t, s[j - 1]), bisect_right(t, s[j - 1])]:
                ans = min(ans, abs(x[i] - s[j - 1]) + abs(s[j - 1] - t[k]))
        for j in [bisect_left(t, x[i]), bisect_right(t, x[i])]:
            for k in [bisect_left(s, t[j]), bisect_right(s, t[j])]:
                ans = min(ans, abs(x[i] - t[j]) + abs(t[j] - s[k]))
            for k in [bisect_left(s, t[j - 1]), bisect_right(s, t[j - 1])]:
                ans = min(ans, abs(x[i] - t[j - 1]) + abs(t[j - 1] - s[k]))
        print(ans)

if __name__ == '__main__':
    main()