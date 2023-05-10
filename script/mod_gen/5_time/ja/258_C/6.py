def main():
    N,Q = map(int,input().split())
    S = input()
    queries = [list(map(str,input().split())) for _ in range(Q)]
    for query in queries:
        if query[0] == '1':
            S = S[N-int(query[1]):] + S[:N-int(query[1])]
        else:
            print(S[int(query[1])-1])

if __name__ == '__main__':
    main()