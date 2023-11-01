def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    m = max(d.values())
    for k in sorted(d.keys()):
        if d[k] == m:
            print(k)
