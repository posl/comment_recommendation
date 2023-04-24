Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    #print(A)
    #print(B)
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                #print(i,j)
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

=======
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    # B の各要素が A のどこにあるかを確認する
    for i in range(H2):
        for j in range(W2):
            if B[i][j] not in A[i]:
                print('No')
                return

    # B の各要素が A のどこにあるかを確認する
    for i in range(H2):
        for j in range(W2):
            if B[i][j] not in A[i]:
                print('No')
                return

    print('Yes')

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

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
Suggestion 4

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    print('Yes' if all([A[i][j] == B[i][j] for i in range(H2) for j in range(W2)]) else 'No')

=======
Suggestion 5

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1):
        for j in range(W1):
            if A[i][j] in [b for a in B for b in a]:
                B[B.index([b for a in B for b in a if a == A[i][j]])//W2][B.index([b for a in B for b in a if a == A[i][j]])%W2] = 0
    if 0 in [b for a in B for b in a]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

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
                    print('Yes')
                    return

    print('No')

=======
Suggestion 7

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    #print(a)
    #print(b)
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            if a[i][j] == b[0][0]:
                #print(i, j)
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')
    return

main()

=======
Suggestion 8

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H2)]
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
                    print('Yes')
                    return
    print('No')

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if B[k][l] != A[i+k][j+l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                print("Yes")
                return
    print("No")
