def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(K):
        A[B[i]-1] = 0
    print(sum(A))
