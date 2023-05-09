def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
        for j in range(i+1, N):
            if ans[j] < ans[j-1] + S[j-1]:
                ans[j] = ans[j-1] + S[j-1]
    for i in range(N):
        print(ans[i])
