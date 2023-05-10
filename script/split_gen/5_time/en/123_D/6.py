def main():
    # Get input
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Sort in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    # Calculate the sum of the deliciousness of the cakes
    # for the first, second, ..., K-th ways
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ans.append(A[i] + B[j] + C[k])
    # Sort in descending order
    ans.sort(reverse=True)
    # Output
    for i in range(K):
        print(ans[i])
