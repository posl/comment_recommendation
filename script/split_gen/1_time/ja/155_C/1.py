def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_count = max(d.values())
    for s, count in d.items():
        if count == max_count:
            print(s)
