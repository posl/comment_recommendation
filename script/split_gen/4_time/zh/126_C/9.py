def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        point = i
        count = 0
        while point < K:
            point *= 2
            count += 1
        ans += (1 / N) * ((1 / 2) ** count)
    print(ans)
