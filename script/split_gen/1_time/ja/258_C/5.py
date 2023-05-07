def main():
    N,Q = map(int,input().split())
    S = input()
    query = [input().split() for i in range(Q)]
    for i in range(Q):
        if query[i][0] == '1':
            S = S[-int(query[i][1]):] + S[:N-int(query[i][1])]
        elif query[i][0] == '2':
            print(S[int(query[i][1])-1])
