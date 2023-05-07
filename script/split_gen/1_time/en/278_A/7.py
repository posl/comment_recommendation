def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #operation
    for i in range(K):
        A[i] = 0
    #output
    print(*A)
