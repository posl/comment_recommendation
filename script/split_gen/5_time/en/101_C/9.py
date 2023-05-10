def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    minnum = min(A)
    minnum_index = A.index(minnum)
    print(int((N-1)/(K-1)) if (N-1)%(K-1)==0 else int((N-1)/(K-1))+1)
