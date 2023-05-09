def main():
    H, W, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    from collections import defaultdict
    d = defaultdict(list)
    for i, (a, b) in enumerate(AB):
        d[a].append((-b, i))
    for k in d:
        d[k].sort()
    for i in range(1, H + 1):
        if i in d:
            for _, j in d[i]:
                print(i, -d[i].pop()[0])
        else:
            print(i, W)
