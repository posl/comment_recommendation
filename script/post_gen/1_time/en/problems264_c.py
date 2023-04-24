Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if all(all(A[i + k][j + l] == B[k][l] for l in range(W2)) for k in range(H2)):
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
                        break
            if flag:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 3

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if all(A[i + k][j + l] == B[k][l] for k in range(H2) for l in range(W2)):
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
    print('Yes' if all(B[i][j] <= A[i][j] for i in range(H2) for j in range(W2)) else 'No')

=======
Suggestion 5

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 6

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
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
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1 < H2 or W1 < W2:
        print("No")
        return
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if all(A[i + k][j + l] == B[k][l] for k in range(H2) for l in range(W2)):
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H_1)]
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H_2)]
    if H_1 > H_2 and W_1 > W_2:
        for i in range(H_1 - H_2 + 1):
            for j in range(W_1 - W_2 + 1):
                if A[i][j] == B[0][0]:
                    for k in range(H_2):
                        for l in range(W_2):
                            if A[i + k][j + l] != B[k][l]:
                                break
                        else:
                            continue
                        break
                    else:
                        print("Yes")
                        return
        print("No")
        return
    print("No")

=======
Suggestion 10

def main():
    H1,W1 = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H1)]
    H2,W2 = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
                        break
                if flag == False:
                    break
            if flag:
                print('Yes')
                return
    print('No')
