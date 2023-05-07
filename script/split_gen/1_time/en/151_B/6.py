def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, M)
    #print(A)
    sumA = sum(A)
    #print(sumA)
    minPoint = M * N - sumA
    #print(minPoint)
    if minPoint <= 0:
        print(0)
    elif minPoint <= K:
        print(minPoint)
    else:
        print(-1)
