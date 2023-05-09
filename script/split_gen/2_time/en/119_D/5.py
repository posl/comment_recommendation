def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(B)] + [10**15]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s1, s2 = get_lr(s, i)
        t1, t2 = get_lr(t, i)
        ans = min(
            max(i - s1, t2 - i),
            max(i - s2, t1 - i),
            max(i - s1, t1 - i) + min(i - s1, t1 - i),
            max(i - s2, t2 - i) + min(i - s2, t2 - i),
            max(i - s1, t2 - i) + min(i - s1, t2 - i),
            max(i - s2, t1 - i) + min(i - s2, t1 - i),
        )
        print(ans)
