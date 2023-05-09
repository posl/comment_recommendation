def main():
    N, K = map(int, input().split())
    S = input()
    L = [0]
    for i in range(1, N):
        if S[i-1] != S[i]:
            L.append(i)
    L.append(N)
    ans = 0
    for i in range(len(L)-1):
        ans += min(L[i+1]-L[i], 2*K+1)
    print(ans)
