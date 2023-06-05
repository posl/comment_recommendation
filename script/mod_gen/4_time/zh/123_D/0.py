def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    # print(A)
    # print(B)
    # print(C)
    ans = []
    for a in range(X):
        for b in range(Y):
            for c in range(Z):
                if (a+1)*(b+1)*(c+1) <= K:
                    ans.append(A[a]+B[b]+C[c])
                else:
                    break
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

if __name__ == '__main__':
    main()