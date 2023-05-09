def main():
    N,Q = map(int,input().split())
    S = input()
    #print(N,Q,S)
    S = list(S)
    #print(S)
    for i in range(Q):
        query = input().split()
        #print(query)
        if query[0] == '1':
            for j in range(int(query[1])):
                S.insert(0,S.pop())
        else:
            print(S[int(query[1])-1])
