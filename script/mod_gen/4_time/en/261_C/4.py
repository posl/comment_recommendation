def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] not in S[:i]:
            print(S[i])
        else:
            cnt = S[:i].count(S[i]) + 1
            print(S[i] + '(' + str(cnt) + ')')

if __name__ == '__main__':
    main()