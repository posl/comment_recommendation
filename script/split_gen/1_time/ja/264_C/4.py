def main():
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))
    for i in range(H1):
        for j in range(W1):
            if A[i][j] == B[0][0]:
                if (i + H2) <= H1 and (j + W2) <= W1:
                    if A[i:i+H2][j:j+W2] == B:
                        print("Yes")
                        return
    print("No")
