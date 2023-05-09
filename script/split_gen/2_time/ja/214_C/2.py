def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [10**10] * N
    for i in range(N):
        for j in range(N):
            if ans[j] > T[i]:
                ans[j] = T[i]
                T[i] += S[j]
                break
    for a in ans:
        print(a)
