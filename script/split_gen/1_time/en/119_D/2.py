def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s1 = s[bisect.bisect_left(s, i)-1]
        s2 = s[bisect.bisect_left(s, i)]
        t1 = t[bisect.bisect_left(t, i)-1]
        t2 = t[bisect.bisect_left(t, i)]
        print(min(abs(i-s1)+abs(s1-t1), abs(i-s1)+abs(s1-t2), abs(i-s2)+abs(s2-t1), abs(i-s2)+abs(s2-t2)))
