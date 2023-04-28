Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                for x in range(H2):
                    for y in range(W2):
                        if A[i+x][j+y] != B[x][y]:
                            break
                    else:
                        continue
                    break
                else:
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

    print('Yes' if is_possible(A, B) else 'No')

=======
Suggestion 3

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 4

def solve():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1 < H2 or W1 < W2:
        print('No')
        return
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
                print('Yes')
                return
    print('No')

=======
Suggestion 5

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h2)]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            for k in range(h2):
                if a[i + k][j:j + w2] != b[k]:
                    break
            else:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            flag = True
            for k in range(h2):
                for l in range(w2):
                    if a[i + k][j + l] != b[k][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 7

def main():
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print('Yes')
                    exit()
    print('No')

=======
Suggestion 8

def main():
    H1, W1 = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(H1)]
    H2, W2 = map(int, input().split())
    B = [[int(i) for i in input().split()] for j in range(H2)]

    print("Yes" if A.count(B) > 0 else "No")

=======
Suggestion 9

def main():
    # Input
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))
    # Processing
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i + k][j + l] != B[k][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    #input
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H_1)]
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H_2)]

    #compute
    for i in range(H_1 - H_2 + 1):
        for j in range(W_1 - W_2 + 1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(H_2):
                    if flag == False:
                        break
                    for l in range(W_2):
                        if A[i + k][j + l] != B[k][l]:
                            flag = False
                            break
                if flag == True:
                    print('Yes')
                    exit()

    print('No')
