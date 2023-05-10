def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1, A[i], B[i], A[i]+B[i]])
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(X):
        ans.append(C[i][0])
    for i in range(X, X+Y):
        ans.append(C[i][0])
    for i in range(X+Y, X+Y+Z):
        ans.append(C[i][0])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()