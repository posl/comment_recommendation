def main():
    H1, W1 = list(map(int, input().split()))
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = list(map(int, input().split()))
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")
