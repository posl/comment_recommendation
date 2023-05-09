def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if (M*N-sum(A)) > K:
        print(-1)
    elif (M*N-sum(A)) < 0:
        print(0)
    else:
        print(M*N-sum(A))
