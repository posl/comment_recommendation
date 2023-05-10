def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1])
    print(' '.join(map(str, [AB[i][0] for i in range(M)])))
