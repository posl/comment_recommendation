def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = [0] * Q
    R = [0] * Q
    X = [0] * Q
    for i in range(Q):
        L[i], R[i], X[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(L[i]-1, R[i]):
            if A[j] == X[i]:
                count += 1
        print(count)
