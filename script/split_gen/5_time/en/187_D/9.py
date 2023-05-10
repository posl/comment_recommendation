def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = 0
    takahashi = 0
    for i, (a, b) in enumerate(AB):
        if i % 2 == 0:
            aoki += a
        else:
            takahashi += b
    print(aoki - takahashi)
