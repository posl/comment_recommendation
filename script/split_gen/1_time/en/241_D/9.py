def main():
    #input
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    
    #process
    #A = []
    A = set()
    ans = []
    for q in query:
        if q[0]==1:
            #A.append(q[1])
            A.add(q[1])
        elif q[0]==2:
            #A.sort()
            #A = sorted(A)
            #print(A)
            #print(A)
            #print(q[1])
            #print(q[2])
            #print(A)
            #print(len(A))
            #print(len([a for a in A if a<=q[1]]))
            #print(A)
            #print([a for a in A if a<=q[1]])
            #print([a for a in A if a<=q[1]][::-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #ans.append([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q
