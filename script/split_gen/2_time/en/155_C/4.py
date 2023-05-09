def main():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    m = max(d.values())
    for k, v in sorted(d.items()):
        if v == m:
            print(k)
