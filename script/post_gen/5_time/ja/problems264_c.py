Synthesizing 10/10 solutions

=======
Suggestion 1

def f():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            if A[i][j] == B[0][0]:
                flg = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i + k][j + l] != B[k][l]:
                            flg = False
                            break
                    if flg == False:
                        break
                if flg:
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 2

def main():
    h1,w1 = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h1)]
    h2,w2 = map(int,input().split())
    b = [list(map(int,input().split())) for _ in range(h2)]

    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            for k in range(h2):
                for l in range(w2):
                    if a[i+k][j+l] != b[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                exit()
    print("No")
main()

=======
Suggestion 3

def solve():
    H1,W1 = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H1)]
    H2,W2 = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(H2)]
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 4

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]

    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                if a[i:i+h2] == b:
                    print('Yes')
                    return

    print('No')

=======
Suggestion 5

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    if h1 < h2 or w1 < w2:
        print('No')
        exit()
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    exit()
    print('No')

=======
Suggestion 6

def main():
    H1, W1 = map(int, input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int, input().split())))

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
Suggestion 7

def main():
    H1, W1 = map(int, input().split())
    A = []
    for _ in range(H1):
        A.append(list(map(int, input().split())))
    H2, W2 = map(int, input().split())
    B = []
    for _ in range(H2):
        B.append(list(map(int, input().split())))

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

main()

=======
Suggestion 8

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j] == B[0][0]:
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    else:
        print('No')
        return

=======
Suggestion 9

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
            for k in range(h2):
                for l in range(w2):
                    if a[i + k][j + l] != b[k][l]:
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                return
    print('No')

=======
Suggestion 10

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                for k in range(h2):
                    if a[i+k][j:j+w2] != b[k]:
                        break
                else:
                    print("Yes")
                    exit()
    print("No")
