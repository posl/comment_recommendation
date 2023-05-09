def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        for j in range(N):
            if ans[(i + j) % N] > ans[i] + S[i]:
                ans[(i + j) % N] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])
