def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] != '!':
            if S[i][0] == S[i+1][0]

if __name__ == '__main__':
    main()