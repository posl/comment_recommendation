def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(B)] + [10**15]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_index = bisect.bisect_right(s, i)
        t_index = bisect.bisect_right(t, i)
        ans = 10**15
        for j in range(s_index-1, s_index+1):
            for k in range(t_index-1, t_index+1):
                ans = min(ans, max(s[j]-i, i-t[k]), max(t[k]-i, i-s[j]))
        print(ans)
