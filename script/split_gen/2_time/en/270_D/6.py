def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    for i in range(1, K):
        if A[i] - A[i-1] > 1:
            print(A[i-1] + 1)
            break
    else:
        print(N)
