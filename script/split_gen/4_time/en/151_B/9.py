def main():
    #input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    #compute
    sum_A = sum(A)
    if N*M > sum_A + K:
        print(-1)
    else:
        if N*M - sum_A > 0:
            print(N*M - sum_A)
        else:
            print(0)
