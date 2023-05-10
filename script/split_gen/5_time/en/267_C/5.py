def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] < 0:
            c += 1
    if m > c:
        a = sorted(a, reverse=True)
        print(sum(a[:m]))
    else:
        a = sorted(a)
        s = 0
        for i in range(m):
            if a[i] < 0:
                s = i
        print(sum(a[s:]))
