def main():
    N = int(input())
    A = []
    for i in range(N):
        L, R = map(int, input().split())
        A.append([L, R])
    A.sort()
    ans = []
    ans.append(A[0])
    for i in range(1, N):
        if A[i][0] < ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], A[i][1])
        else:
            ans.append(A[i])
    for i in ans:
        print(i[0], i[1])
