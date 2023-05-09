def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_value = max(d.values())
    for k, v in sorted(d.items(), key=lambda x:x[0]):
        if v == max_value:
            print(k)
