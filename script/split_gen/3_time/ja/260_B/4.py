def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i]+B[i], A[i], B[i], i+1])
    C.sort(reverse=True)
    ans = []
    for i in range(X):
        ans.append(C[i][3])
    for i in range(X, X+Y):
        if C[i][1] > C[i][2]:
            ans.append(C[i][3])
    for i in range(X+Y, X+Y+Z):
        ans.append(C[i][3])
    ans.sort()
    for i in ans:
        print(i)
