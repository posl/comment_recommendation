Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
                    print("Yes")
                    return
    print("No")

=======
Suggestion 2

def main():
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    for i in range(h1):
        for j in range(w1):
            if a[i][j] in b:
                b.remove(a[i][j])
    if len(b) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h2)]
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
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
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
Suggestion 5

def main():
    pass

=======
Suggestion 6

def solve():
    H1,W1 = map(int,input().split())
    A = []
    for _ in range(H1):
        A.append(list(map(int,input().split())))
    H2,W2 = map(int,input().split())
    B = []
    for _ in range(H2):
        B.append(list(map(int,input().split())))
    if H1<H2 or W1<W2:
        print("No")
        return
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if A[i][j]==B[0][0]:
                flag = True
                for k in range(H2):
                    for l in range(W2):
                        if A[i+k][j+l]!=B[k][l]:
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
            if a[i][j] == b[0][0]:
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] == b[k][l]:
                            continue
                        else:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 8

def solve(h1, w1, a, h2, w2, b):
    #print(h1, w1, a, h2, w2, b)
    if h1 < h2 or w1 < w2:
        return False
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                #print(a[i][j], b[0][0])
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                            break
                    if flag == False:
                        break
                if flag == True:
                    return True
    return False

h1, w1 = map(int, input().split())
a = []
for i in range(h1):
    a.append(list(map(int, input().split())))
h2, w2 = map(int, input().split())
b = []
for i in range(h2):
    b.append(list(map(int, input().split())))
