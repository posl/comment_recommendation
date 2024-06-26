def main():
    N = int(input())
    S = input()
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(N):
        if S[i] == 'R':
            R[i+1] = R[i] + 1
            G[i+1] = G[i]
            B[i+1] = B[i]
        if S[i] == 'G':
            R[i+1] = R[i]
            G[i+1] = G[i] + 1
            B[i+1] = B[i]
        if S[i] == 'B':
            R[i+1] = R[i]
            G[i+1] = G[i]
            B[i+1] = B[i] + 1
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] != S[j]:
                if j - i == (j - i)*2:
                    if S[j - i] != S[j]:
                        ans += 1
                else:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()