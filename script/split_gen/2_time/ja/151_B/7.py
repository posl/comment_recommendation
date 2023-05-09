def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if N*M - sum_A <= K:
        if N*M - sum_A > 0:
            print(N*M - sum_A)
        else:
            print(0)
    else:
        print(-1)
