def solve():
    N = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(N)]
    total_a = sum(a for a, b in AB)
    total_b = sum(b for a, b in AB)
    total_time = total_a / total_b
    time = 0
    for a, b in AB:
        time += a / b
        if time >= total_time / 2:
            print(time)
            break
