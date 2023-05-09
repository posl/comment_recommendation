def main():
    #input
    N,P,Q,R,S=map(int,input().split())
    A=list(map(int,input().split()))
    #output
    print(' '.join(map(str,A[P-1:Q]+A[R-1:S])))
