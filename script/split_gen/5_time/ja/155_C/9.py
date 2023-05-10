def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    max = 0
    for x in d:
        if d[x] > max:
            max = d[x]
    for x in sorted(d):
        if d[x] == max:
            print(x)
