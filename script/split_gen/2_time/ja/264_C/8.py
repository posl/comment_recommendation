def main():
    H1, W1 = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [[int(x) for x in input().split()] for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")
