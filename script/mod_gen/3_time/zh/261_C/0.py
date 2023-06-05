def main():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    for i in range(n):
        if S[i] in S[:i]:
            j = S[:i].count(S[i])
            print(S[i] + '(' + str(j + 1) + ')')
        else:
            print(S[i])

if __name__ == '__main__':
    main()