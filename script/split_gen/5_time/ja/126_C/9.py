def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
        else:
            tmp = 1
            while i < K:
                i *= 2
                tmp /= 2
            ans += tmp / N
    print(ans)
