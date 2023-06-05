def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
        if b not in d:
            d[b] = [a]
        else:
            d[b].append(a)
    for i in range(1, n+1):
        if i in d:
            d[i].sort()
            print(len(d[i]), end=' ')
            for j in d[i]:
                print(j, end=' ')
            print()
        else:
            print(0)
