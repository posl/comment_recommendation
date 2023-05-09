def main():
    N = int(input())
    S = input()
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(N):
        if S[i] == 'R':
            R[i+1] = R[i]+1
            G[i+1] = G[i]
            B[i+1] = B[i]
        elif S[i] == 'G':
            R[i+1] = R[i]
            G[i+1] = G[i]+1
            B[i+1] = B[i]
        elif S[i] == 'B':
            R[i+1] = R[i]
            G[i+1] = G[i]
            B[i+1] = B[i]+1
    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if S[i-1] != S[j-1]:
                if j + (j-i) <= N:
                    if S[j-1] != S[j+(j-i)-1] and S[i-1] != S[j+(j-i)-1]:
                        ans += 1
                if j - (j-i) >= 1:
                    if S[j-1] != S[j-(j-i)-1] and S[i-1] != S[j-(j-i)-1]:
                        ans += 1
    ans += (R[N]-R[0])*(G[N]-G[0])*(B[N]-B[0])
    print(ans)
