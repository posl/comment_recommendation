def main():
    import bisect
    q = int(input())
    a = []
    b = []
    for i in range(q):
        p, x = map(int, input().split())
        if p == 1:
            bisect.insort(a, x)
        elif p == 2:
            b.append(x)
        else:
            print(a[0] + sum(b))
            a.pop(0)
    return
