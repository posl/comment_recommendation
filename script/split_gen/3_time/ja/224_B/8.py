def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i < k and j < l:
                        if A[i][j] + A[k][l] > A[k][j] + A[i][l]:
                            print("No")
                            return
    print("Yes")
    return
