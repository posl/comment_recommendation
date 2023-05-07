def main():
    N,Q = map(int, input().split())
    S = input()
    S = list(S)
    #print(S)
    query = [list(map(str, input().split())) for _ in range(Q)]
    
    for q in query:
        if q[0] == "1":
            for i in range(int(q[1])):
                tmp = S.pop()
                S.insert(0, tmp)
        else:
            print(S[int(q[1])-1])
