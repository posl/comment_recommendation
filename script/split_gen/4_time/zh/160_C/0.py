def main():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    max_distance = 0
    for i in range(N-1):
        if A[i+1]-A[i] > max_distance:
            max_distance = A[i+1]-A[i]
    if K-A[-1]+A[0] > max_distance:
        max_distance = K-A[-1]+A[0]
    print(K-max_distance)
