def main():
    N = int(input())
    S = input()
    R = [0]
    G = [0]
    B = [0]
    for i in range(N):
        R.append(R[i] + (S[i] == "R"))
        G.append(G[i] + (S[i] == "G"))
        B.append(B[i] + (S[i] == "B"))
    ans = R[-1] * G[-1] * B[-1]
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k < N and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()