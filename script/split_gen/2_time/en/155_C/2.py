def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_val = max(d.values())
    for key, val in sorted(d.items()):
        if val == max_val:
            print(key)
