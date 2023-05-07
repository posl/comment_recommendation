def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_v = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_v:
            print(k)
