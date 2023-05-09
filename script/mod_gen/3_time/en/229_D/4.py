def main():
    S = input()
    K = int(input())
    N = len(S)
    X = 0
    for i in range(N):
        if S[i] == 'X':
            X += 1
    Y = N - X
    if Y <= K:
        print(N)
    else:
        L = []
        for i in range(N):
            if S[i] == '.':
                L.append(i)
        L.append(N)
        M = len(L)
        ans = 0
        for i in range(M - 1):
            ans = max(ans, L[i + 1] - L[i])
        print(ans - 1)

if __name__ == '__main__':
    main()