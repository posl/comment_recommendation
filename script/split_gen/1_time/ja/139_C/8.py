def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            H[i + 1] = H[i]
        else:
            ans = max(ans, H[i + 1] - H[i])
    print(ans)
