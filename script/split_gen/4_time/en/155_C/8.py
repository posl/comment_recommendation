def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    from collections import Counter
    c = Counter(S)
    max_count = max(c.values())
    for k, v in c.items():
        if v == max_count:
            print(k)
