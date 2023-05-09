def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    battery = N
    prev_b = 0
    for a, b in AB:
        battery -= a - prev_b
        if battery <= 0:
            print("No")
            exit()
        battery += b - a
        battery = min(battery, N)
        prev_b = b
    battery -= T - prev_b
    if battery <= 0:
        print("No")
        exit()
    print("Yes")

if __name__ == '__main__':
    main()