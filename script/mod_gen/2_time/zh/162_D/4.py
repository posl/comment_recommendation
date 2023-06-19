def main():
    N = int(input())
    S = input()
    R = [0] * N
    G = [0] * N
    B = [0] * N
    for i in range(N):
        if i != 0:
            R[i] = R[i-1]
            G[i] = G[i-1]
            B[i] = B[i-1]
        if S[i] == 'R':
            R[i] += 1
        elif S[i] == 'G':
            G[i] += 1
        else:
            B[i] += 1
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i] != S[j]:
                if S[i] != S[j+j-i]:
                    if S[j] != S[j+j-i]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()