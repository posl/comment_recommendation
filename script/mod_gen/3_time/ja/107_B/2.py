def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = []
    for i in range(H):
        if "#" in A[i]:
            B.append(A[i])
    C = []
    for i in range(len(B[0])):
        flag = True
        for j in range(len(B)):
            if B[j][i] == "#":
                flag = False
                break
        if flag:
            C.append(i)
    for i in range(len(B)):
        for j in range(len(C)):
            del B[i][C[j]-j]
    for i in range(len(B)):
        print("".join(B[i]))
main()
