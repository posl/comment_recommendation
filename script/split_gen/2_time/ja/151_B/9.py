def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    #print(sumA)
    need = N * M - sumA
    #print(need)
    if need <= K:
        print(max(0, need))
    else:
        print(-1)
