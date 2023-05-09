def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K)
    d = []
    for i in range(N):
        d.append(A[i+1]-A[i])
    d.append(K-A[N]+A[0])
    print(K-max(d))
