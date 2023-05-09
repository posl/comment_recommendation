def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_v = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_v:
            print(k)
