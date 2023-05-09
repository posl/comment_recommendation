def main():
    from collections import defaultdict
    N, M = map(int, input().split())
    d = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    for i in range(1, N+1):
        print(len(d[i]), *sorted(d[i]))
