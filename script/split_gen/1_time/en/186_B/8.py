def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    #print(A)
    minA = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < minA:
                minA = A[i][j]
    #print(minA)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)
