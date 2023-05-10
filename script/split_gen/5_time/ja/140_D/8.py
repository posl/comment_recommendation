def main():
    N, K = map(int, input().split())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
        else:
            R.append(i)
    ans = 0
    for i in range(len(L)):
        if i == 0:
            ans += L[i]
        else:
            ans += L[i] - L[i - 1] - 1
    for i in range(len(R)):
        if i == 0:
            ans += R[i]
        else:
            ans += R[i] - R[i - 1] - 1
    ans += len(L) + len(R)
    ans -= 1
    ans = min(ans, N - 1)
    print(ans)
