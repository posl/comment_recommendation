def solve():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    battery = N
    prev = 0
    for a, b in AB:
        battery -= a - prev
        if battery <= 0:
            print("No")
            return
        battery += b - a
        battery = min(N, battery)
        prev = b
    battery -= T - prev
    if battery <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()