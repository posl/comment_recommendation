def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S_max = S.count(S[-1])
    for i in range(N):
        if S_max == S.count(S[i]):
            print(S[i])

if __name__ == '__main__':
    main()