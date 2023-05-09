def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
        else:
            j = i
            while j < K:
                j *= 2
                ans += 1/N
    print(ans/N)
