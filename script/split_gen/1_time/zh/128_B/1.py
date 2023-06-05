def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, p = input().split()
        p = int(p)
        if s in d:
            d[s].append(p)
        else:
            d[s] = [p]
    for k in sorted(d):
        for v in sorted(d[k], reverse=True):
            print(d[k].index(v)+1)
