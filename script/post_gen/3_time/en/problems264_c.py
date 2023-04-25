Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    # 2次元累積和
    S1 = [[0] * (W1 + 1) for _ in range(H1 + 1)]
    S2 = [[0] * (W2 + 1) for _ in range(H2 + 1)]
    for i in range(H1):
        for j in range(W1):
            S1[i + 1][j + 1] = S1[i][j + 1] + S1[i + 1][j] - S1[i][j] + A[i][j]
    for i in range(H2):
        for j in range(W2):
            S2[i + 1][j + 1] = S2[i][j + 1] + S2[i + 1][j] - S2[i][j] + B[i][j]

    # 2次元累積和の差分
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if S1[i + H2][j + W2] - S1[i + H2][j] - S1[i][j + W2] + S1[i][j] == S2[H2][W2]:
                print("Yes")
                return

    print("No")

=======
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    print("Yes" if H1 >= H2 and W1 >= W2 and all([all([A[i][j] >= B[i][j] for j in range(W2)]) for i in range(H2)]) else "No")

=======
Suggestion 4

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    if h1 < h2 or w1 < w2:
        print('No')
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if all(a[i + k][j + l] == b[k][l] for k in range(h2) for l in range(w2)):
                print('Yes')
                return
    print('No')

=======
Suggestion 5

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H2)]
    #print(A)
    #print(B)
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            #print(i,j)
            A[i][j] = A[i][j] - B[0][0]
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != A[i][j] + B[k][l]:
                        #print(A[i+k][j+l], A[i][j] + B[k][l])
                        print('No')
                        return
    print('Yes')
    return

=======
Suggestion 6

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
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return

    print("No")

=======
Suggestion 7

def main():
    H1, W1 = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(H1)]
    H2, W2 = [int(x) for x in input().split()]
    B = [[int(x) for x in input().split()] for _ in range(H2)]
    for i in range(H1):
        for j in range(W1):
            if i < H2 and j < W2:
                if A[i][j] != B[i][j]:
                    print('No')
                    return
            elif i < H2 or j < W2:
                print('No')
                return
    print('Yes')

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    # Read the input
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))
    # Check if it is possible to make A equal B
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i + k][j + l] != B[k][l]:
                        flag = False
            if flag:
                print("Yes")
                return
    print("No")
    return

main()

=======
Suggestion 10

def input_list(): return list(map(int, input().split()))
