def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            continue
        if S[i][0] == '!' and S[i+1][0] != '!':
            if S[i][1:] == S[i+1]:
                print(S[i][1:])
                return
        if S[i][0] != '!' and S[i+1][0] == '!':
            if S[i] == S[i+1][1:]:
                print(S[i])
                return
    print('satisfiable')

if __name__ == '__main__':
    main()