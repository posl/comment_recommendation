def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K)
    A.append(K+A[1])
    A.sort()
    min = K
    for i in range(N):
        if A[i+1] - A[i] < min:
            min = A[i+1] - A[i]
    print(min)
