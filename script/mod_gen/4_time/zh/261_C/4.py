def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if i == 0:
            print(S[i])
        else:
            if S[i] in S[:i]:
                cnt = S[:i].count(S[i])
                print(S[i] + "(" + str(cnt) + ")")
            else:
                print(S[i])

if __name__ == '__main__':
    main()