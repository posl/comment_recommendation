def main():
    #input
    N,Q = map(int,input().split())
    S = input()
    l = [0]*Q
    r = [0]*Q
    for i in range(Q):
        l[i],r[i] = map(int,input().split())
    
    #solve
    count = [0]*(N+1)
    for i in range(1,N):
        if S[i-1:i+1] == "AC":
            count[i+1] = count[i] + 1
        else:
            count[i+1] = count[i]
    
    #output
    for i in range(Q):
        print(count[r[i]]-count[l[i]])
