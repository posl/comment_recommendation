def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N*M <= sum(A):
        print(0)
    elif N*M - K <= sum(A):
        print(N*M - sum(A))
    else:
        print(-1)
