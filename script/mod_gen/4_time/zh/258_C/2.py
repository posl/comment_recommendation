def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(int, input().split())) for _ in range(Q)]
    for t, x in query:
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

if __name__ == '__main__':
    main()