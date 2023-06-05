def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    for i in range(N):
        print(A[i], end=' ')
    print()
