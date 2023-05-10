def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
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

if __name__ == '__main__':
    main()