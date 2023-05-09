def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if K >= a - ans:
            K += b
            ans = a
    print(ans + K)
