def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    S3 = []
    for i in range(N):
        if S[i] not in S2:
            S2.append(S[i])
            S3.append(0)
        else:
            S3[S2.index(S[i])] += 1
            S2.append(S[i])
            S3.append(0)
    for i in range(N):
        if S3[S2.index(S[i])] == 0:
            print(S[i])
        else:
            print(S[i] + '(' + str(S3[S2.index(S[i])]) + ')')

if __name__ == '__main__':
    main()