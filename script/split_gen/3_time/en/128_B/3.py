def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, p = input().split()
        p = int(p)
        if s in d:
            d[s].append((-p, i+1))
        else:
            d[s] = [(-p, i+1)]
    for k in sorted(d.keys()):
        for p, i in sorted(d[k]):
            print(i)
