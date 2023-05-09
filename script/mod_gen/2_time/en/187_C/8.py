def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S.append('')
    for i in range(N):
        if S[i][0] == '!':
            if S[i] == S[i+1]:
                print(S[i][1:])
                return
    print('satisfiable')

if __name__ == '__main__':
    main()