def main():
    from bisect import bisect_left, bisect_right
    q = int(input())
    a = []
    for _ in range(q):
        c, *x = map(int, input().split())
        if c == 1:
            a.append(x[0])
        else:
            x, k = x
            if c == 2:
                i = bisect_left(a, x)
                if i + k - 1 < len(a):
                    print(a[i + k - 1])
                else:
                    print(-1)
            else:
                i = bisect_right(a, x)
                if i - k >= 0:
                    print(a[i - k])
                else:
                    print(-1)
