def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [input().split() for _ in range(Q)]
    for query in queries:
        t, x = int(query[0]), int(query[1])
        if t == 1:
            S = S[-x:] + S[:N-x]
        elif t == 2:
            print(S[x-1])

if __name__ == '__main__':
    main()