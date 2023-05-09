def main():
    N, K, X = map(int, input().split())
    A = [int(x) for x in input().split()]
    sum = 0
    for i in range(0,N):
        if A[i] < K:
            sum += A[i]
        else:
            sum += K
    print(sum)
