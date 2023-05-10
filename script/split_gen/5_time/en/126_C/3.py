def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            x = i
            j = 0
            while x < K:
                x *= 2
                j += 1
            ans += (1/N) * (1/2)**j
    print(ans)
