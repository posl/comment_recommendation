def main():
    N = int(input())
    S = [input() for i in range(N)]
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = 1
            print(S[i])
        else:
            print(S[i] + "(" + str(d[S[i]]) + ")")
            d[S[i]] += 1

if __name__ == '__main__':
    main()