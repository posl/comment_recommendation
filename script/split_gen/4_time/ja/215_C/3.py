def main():
    from collections import Counter
    from itertools import permutations
    s, k = input().split()
    k = int(k)
    n = len(s)
    c = Counter(s)
    l = []
    for i in range(1, n + 1):
        for p in permutations(s, i):
            l.append(p)
    l = sorted(set(l))
    ans = l[k - 1]
    print("".join(ans))
