def main():
    N,Q = map(int,input().split())
    S = input()
    queries = []
    for i in range(Q):
        queries.append(list(input().split()))
    for i in range(Q):
        if queries[i][0] == '1':
            S = S[N-int(queries[i][1]):] + S[:N-int(queries[i][1])]
        else:
            print(S[int(queries[i][1])-1])
