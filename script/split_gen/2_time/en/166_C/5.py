def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        ans += 1
        for a, b in AB:
            if a == i + 1 and H[i] <= H[b - 1]:
                ans -= 1
                break
            elif b == i + 1 and H[i] <= H[a - 1]:
                ans -= 1
                break
    print(ans)
