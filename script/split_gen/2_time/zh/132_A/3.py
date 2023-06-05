def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')
