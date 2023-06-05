def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S:
                print(S[i][1:])
                return
        else:
            if '!' + S[i] in S:
                print(S[i])
                return
    print('satisfiable')

if __name__ == '__main__':
    main()