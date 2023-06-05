def main():
    N,K,D=map(int,input().split())
    A=list(map(int,input().split()))
    #print(N,K,D)
    #print(A)
    S=[]
    for i in range(N-K+1):
        S.append(sum(A[i:i+K]))
    print(S)
    S=[i for i in S if i%D!=0]
    print(S)
    if len(S)==0:
        print(-1)
    else:
        print(max(S))
