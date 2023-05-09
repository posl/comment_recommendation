def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    h = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        h[a - 1] = max(h[a - 1], H[b - 1])
        h[b - 1] = max(h[b - 1], H[a - 1])
    ans = 0
    for i in range(N):
        if H[i] > h[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()