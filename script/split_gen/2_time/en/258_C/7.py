def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(queries)
    #print(S)
    #print(N, Q)
    #print(S)
    #print(queries)
    for query in queries:
        if query[0] == 1:
            S = S[-1] + S[:-1]
        else:
            print(S[query[1]-1])
