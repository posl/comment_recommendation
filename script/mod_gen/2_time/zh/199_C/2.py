def solve(n, s, q, query):
    #print("n,s,q,query=",n,s,q,query)
    #print("s[0:n]=",s[0:n])
    #print("s[n:2*n]=",s[n:2*n])
    #print("s=",s)
    for i in range(q):
        #print("i=",i)
        #print("query[i][0]=",query[i][0])
        #print("query[i][1]=",query[i][1])
        #print("query[i][2]=",query[i][2])
        if query[i][0] == 1:
            #print("s[query[i][1]-1]=",s[query[i][1]-1])
            #print("s[query[i][2]-1]=",s[query[i][2]-1])
            #print("s[query[i][1]-1],s[query[i][2]-1]=",s[query[i][1]-1],s[query[i][2]-1])
            s[query[i][1]-1], s[query[i][2]-1] = s[query[i][2]-1], s[query[i][1]-1]
            #print("s[query[i][1]-1],s[query[i][2]-1]=",s[query[i][1]-1],s[query[i][2]-1])
        elif query[i][0] == 2:
            #print("s[0:n]=",s[0:n])
            #print("s[n:2*n]=",s[n:2*n])
            s[0:n], s[n:2*n] = s[n:2*n], s[0:n]
            #print("s[0:n]=",s[0:n])
            #print("s[n:2*n]=",s[n:2*n])
    return s

if __name__ == '__main__':
    solve()