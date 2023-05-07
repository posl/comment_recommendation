def main():
    from itertools import permutations
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for p in permutations(s):
        x = '_'.join(p)
        if len(x) < 3 or len(x) > 16 or x in t:
            continue
        print(x)
        return
    print(-1)
