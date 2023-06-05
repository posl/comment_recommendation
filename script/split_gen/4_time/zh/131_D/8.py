def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print("No")
            return
    print("Yes")
solve()
