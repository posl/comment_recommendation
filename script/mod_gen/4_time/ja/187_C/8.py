def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N):
        if S[i][0] != '!':
            if S[i][1:] in S[i+1:]:
                print(S[i][1:])
                exit()
    print('satisfiable')

if __name__ == '__main__':
    main()