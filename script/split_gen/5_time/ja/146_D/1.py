def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    d = {}
    for a, b in ab:
        d.setdefault(a, [])
        d[a].append(b)
        d.setdefault(b, [])
        d[b].append(a)
    c = [0] * n
    c[0] = 1
    c[1] = 2
    c[2] = 3
    c[3] = 4
    for i in range(4, n):
        c[i] = i+1
    for i in range(1, n+1):
        for j in d[i]:
            if c[i-1] == c[j-1]:
                c[j-1] += 1
    print(max(c))
    for i in c:
        print(i)
