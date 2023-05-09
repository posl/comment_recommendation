def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    A.append(A[0]+K)
    max_dist = 0
    for i in range(N):
        max_dist = max(max_dist, A[i+1]-A[i])
    # output
    print(K-max_dist)
