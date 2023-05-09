def main():
    N, Q = map(int, input().split())
    S = input()
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))
    #print(N, Q)
    #print(S)
    #print(query)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(N, Q)
    #print(S)
    #print(query)
    for i in range(Q):
        if query[i][0] == '1':
            S = S[N-1] + S[0:N-1]
            #print(S)
        else:
            print(S[int(query[i][1])-1])

if __name__ == '__main__':
    main()