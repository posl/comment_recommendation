def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    current = 1
    for i in range(K):
        current = A[current - 1]
    print(current)
