def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    for i in range(N):
        if S[i][0] == '!':
            S[i] = S[i][1:]
            if S[i] in S:
                print(S[i])
                break
        else:
            if '!' + S[i] in S:
                print(S[i])
                break
    else:
        print('satisfiable')

if __name__ == '__main__':
    main()