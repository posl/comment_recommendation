def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int,input().split()))
        l.pop(0)
        d.setdefault(tuple(l),0)
        d[tuple(l)] += 1
    print(len(d))
