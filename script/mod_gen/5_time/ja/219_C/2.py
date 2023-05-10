def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(len(S[i])):
            S[i] = S[i].replace(S[i][j], chr(97 + X.index(S[i][j])))
    S.sort()
    for i in range(N):
        for j in range(len(S[i])):
            S[i] = S[i].replace(S[i][j], X[ord(S[i][j]) - 97])
    for i in range(N):
        print(S[i])

if __name__ == '__main__':
    main()