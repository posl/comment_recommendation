def main():
    n = int(input())
    v = [int(x) for x in input().split(' ')]
    c = [int(x) for x in input().split(' ')]
    res = 0
    for i in range(1 << n):
        s1, s2 = 0, 0
        for j in range(n):
            if (i >> j) & 1:
                s1 += v[j]
                s2 += c[j]
        res = max(res, s1 - s2)
    print(res)
