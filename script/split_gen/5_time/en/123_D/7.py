def main():
    # Get input here
    X, Y, Z, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    # Compute result here
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1) <= K:
                    ans.append(A[i]+B[j]+C[k])
                else:
                    break
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])
