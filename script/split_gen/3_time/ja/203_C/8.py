def solve():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([10**100, 0])
    current = 0
    for a, b in AB:
        if current + K < a:
            break
        K += b
        current = a
    print(current+K)
