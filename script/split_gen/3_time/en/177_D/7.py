def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [[a-1, b-1] for a, b in AB]
    AB = [[a, b] if a < b else [b, a] for a, b in AB]
    AB = list(set([tuple(a) for a in AB]))
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1])
    d = {}
    for a, b in AB:
        if a not in d:
            d[a] = []
        d[a].append(b)
    ans = 0
    while len(d) > 0:
        ans += 1
        k = list(d.keys())[0]
        q = [k]
        while len(q) > 0:
            k = q.pop()
            if k in d:
                for v in d[k]:
                    q.append(v)
                del d[k]
    print(ans)
