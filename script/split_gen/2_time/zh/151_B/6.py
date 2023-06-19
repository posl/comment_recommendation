def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*K-sum(A)<0:
        print(0)
    elif N*K-sum(A)>M:
        print(-1)
    else:
        print(N*K-sum(A))
