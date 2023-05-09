def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
            print(S[i] + '(' + str(d[S[i]]) + ')')
        else:
            d[S[i]] = 0
            print(S[i])

if __name__ == '__main__':
    main()