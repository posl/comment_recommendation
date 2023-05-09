def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    perm = [i for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((x[perm[i]] - x[perm[j]]) ** 2 + (y[perm[i]] - y[perm[j]]) ** 2) ** 0.5
    for i in range(2, N + 1):
        ans /= i
    print(ans)
