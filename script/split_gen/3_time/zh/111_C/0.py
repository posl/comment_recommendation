def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = 0
    c2 = 0
    for i in range(1, n // 2 + 1):
        if v1.count(i) > v1.count(i + 1):
            c1 += v1.count(i + 1)
            c2 += v2.count(i)
        else:
            c1 += v1.count(i)
            c2 += v2.count(i + 1)
    print(n - max(c1, c2) * 2)
