def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while i < K:
        i += 1
        A = A[A[i-1]-1:]
        if len(A) == 0:
            break
    print(A[0])
