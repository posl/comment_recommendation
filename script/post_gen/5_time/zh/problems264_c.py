Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

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
Suggestion 3

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
Suggestion 4

def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))

    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            if A[i][j] == B[0][0]:
                #print("A[{}][{}] == B[{}][{}]".format(i, j, 0, 0))
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 5

def main():
    return 0

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
    if h1 < h2 or w1 < w2:
        print('No')
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
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

=======
Suggestion 7

def main():
    h1,w1 = map(int,input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int,input().split())))
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            temp = []
            for k in range(h2):
                temp.append(a[i+k][j:j+w2])
            if temp == b:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            a = []
            for k in range(h2):
                a.append(A[i + k][j:j + w2])
            if a == B:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 9

def matrix_equal(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                return False
            else:
                for j in range(len(a[i])):
                    if a[i][j] != b[i][j]:
                        return False
        return True
