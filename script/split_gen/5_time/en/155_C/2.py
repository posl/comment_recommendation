def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    d = {}
    for i in s:
        d.setdefault(i, 0)
        d[i] += 1
    m = max(d.values())
    for i in d:
        if d[i] == m:
            print(i)
