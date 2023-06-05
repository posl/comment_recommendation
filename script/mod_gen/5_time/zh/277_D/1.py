def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + m)
    s = 0
    for i in range(n):
        d = a[i + 1] - a[i]
        if d <= 0:
            continue
        s += d
        a[i + 1] -= d
    print(s)
main()
