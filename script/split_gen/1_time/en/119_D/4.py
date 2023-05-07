def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_i = bisect.bisect_right(s, i)
        t_i = bisect.bisect_right(t, i)
        s_l = s[s_i-1]
        s_r = s[s_i]
        t_l = t[t_i-1]
        t_r = t[t_i]
        dist = min(abs(i-s_l)+abs(t_l-s_l), abs(i-s_l)+abs(t_r-s_l), abs(i-s_r)+abs(t_l-s_r), abs(i-s_r)+abs(t_r-s_r))
        print(dist)
