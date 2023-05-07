def processQueries(N, Q, S, queries):
    for query in queries:
        if query[0] == 1:
            S = S[-query[1]:] + S[:-query[1]]
        else:
            print(S[query[1]-1])

if __name__ == '__main__':
    processQueries()