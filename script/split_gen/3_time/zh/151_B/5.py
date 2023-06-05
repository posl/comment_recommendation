def main():
    N,K,M = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    if N*M-sum(A)>K:
        print(-1)
    else:
        print(max(N*M-sum(A),0))
