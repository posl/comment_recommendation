def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = 1
            print(S[i])
        else:
            d[S[i]] += 1
            print(S[i] + "(" + str(d[S[i]]-1) + ")")

if __name__ == '__main__':
    main()