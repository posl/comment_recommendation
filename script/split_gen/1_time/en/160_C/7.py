def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    A.sort()
    dist = 0
    for i in range(N):
        dist = max(dist, A[i+1]-A[i])
    print(K-dist)
