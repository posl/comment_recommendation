def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = []
    for i in range(N):
        if S[i] not in ans:
            ans.append(S[i])
            print(S[i])
        else:
            num = ans.count(S[i])
            ans.append(S[i])
            print(S[i] + '(' + str(num) + ')')

if __name__ == '__main__':
    main()