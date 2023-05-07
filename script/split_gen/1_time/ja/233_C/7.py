def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L[1:])
    #print(A)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(len(A[i])):
                for l in range(len(A[j])):
                    if A[i][k] * A[j][l] == X:
                        cnt += 1
    print(cnt)
