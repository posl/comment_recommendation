def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] in S[:i]:
            count = 0
            for j in range(i):
                if S[i] == S[j]:
                    count += 1
            print(S[i] + '(' + str(count) + ')')
        else:
            print(S[i])

if __name__ == '__main__':
    main()