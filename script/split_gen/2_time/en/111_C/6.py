def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    a = sorted(a)
    b = sorted(b)
    if a[0] != a[-1] and b[0] != b[-1]:
        print(min(len(a) - a.count(a[0]), len(b) - b.count(b[0])))
    elif a[0] != a[-1]:
        print(len(a) - a.count(a[0]))
    elif b[0] != b[-1]:
        print(len(b) - b.count(b[0]))
    else:
        print(n // 2)
