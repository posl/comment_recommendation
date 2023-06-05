def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    total=sum(A)
    if A[M-1]*4*M>=total:
        print("是")
    else:
        print("否")
