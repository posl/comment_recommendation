def main():
    H, W, C = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(H):
        for j in range(W):
            B.append([A[i][j], i, j])
    B.sort()
    ans = 10**18
    for i in range(H*W):
        for j in range(i+1, H*W):
            ans = min(ans, B[i][0]+B[j][0]+C*(abs(B[i][1]-B[j][1])+abs(B[i][2]-B[j][2])))
    print(ans)
main()
