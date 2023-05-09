def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    for i in range(N):
        if S[i] in S2:
            S[i] = S[i] + "(" + str(S2.count(S[i])) + ")"
            S2.append(S[i])
        else:
            S2.append(S[i])
    for i in range(N):
        print(S[i])

if __name__ == '__main__':
    main()