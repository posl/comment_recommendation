def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    s = sum(a)
    for i in range(q):
        b, c = bc[i]
        if b in d:
            s += d[b] * (c - b)
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            d[b] = 0
        print(s)
