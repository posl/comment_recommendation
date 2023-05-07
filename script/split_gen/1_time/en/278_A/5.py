def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        if i == 0:
            A = A[1:]
            A.append(0)
        else:
            A = A[1:]
            A.append(0)
    print(' '.join(map(str, A)))
