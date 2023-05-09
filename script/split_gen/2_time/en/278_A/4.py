def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        if i < N:
            A[i] = 0
        else:
            A.append(0)
    print(' '.join(map(str, A)))
