def main():
    import itertools
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = -1
    for p in itertools.permutations(s):
        for i in range(1, n):
            for j in range(1, 17 - len(p[i])):
                x = p[0] + '_' * j + p[i]
                if x not in t:
                    ans = x
                    break
            if ans != -1:
                break
        if ans != -1:
            break
    print(ans)
