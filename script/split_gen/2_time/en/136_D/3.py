def main():
    S = input()
    N = len(S)
    L = [0 for _ in range(N+1)]
    R = [0 for _ in range(N+1)]
    for i in range(N):
        if S[i] == 'L':
            L[i+1] = L[i] + 1
        else:
            R[i+1] = R[i] + 1
    ans = [0 for _ in range(N)]
    for i in range(N):
        if S[i] == 'L':
            ans[i] += R[i] + 1 - (L[i] + 1) // 2
            ans[i-1] += (L[i] + 1) // 2
        else:
            ans[i] += L[i+1] - R[i] // 2
            ans[i+1] += R[i] // 2
    print(*ans)
