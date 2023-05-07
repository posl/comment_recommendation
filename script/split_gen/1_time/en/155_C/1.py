def main():
    N = int(input())
    S = [input() for i in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    m = max(d.values())
    for s in sorted(d.keys()):
        if d[s] == m:
            print(s)
