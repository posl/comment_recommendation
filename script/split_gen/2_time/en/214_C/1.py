def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i + 1, i + N):
            if ans[j % N] > ans[(j - 1) % N] + S[(j - 1) % N]:
                ans[j % N] = ans[(j - 1) % N] + S[(j - 1) % N]
    for i in range(N):
        print(ans[i])
