def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    for i in range(N):
        if S[i][0] == '!':
            if S[i][1:] in S_set:
                print(S[i][1:])
                break
        else:
            if '!' + S[i] in S_set:
                print(S[i])
                break
    else:
        print('satisfiable')

if __name__ == '__main__':
    main()