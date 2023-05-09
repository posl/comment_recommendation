Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
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
                if A[i + k][j:j + W2] != B[k]:
                    break
            else:
                print('Yes')
                return

    print('No')

=======
Suggestion 2

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

    print('Yes' if a.count(b[0]) > 0 else 'No')

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
Suggestion 4

def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]

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
Suggestion 5

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
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                if flag:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 6

def readinput():
    h1,w1=list(map(int,input().split()))
    a=[]
    for _ in range(h1):
        row=list(map(int,input().split()))
        a.append(row)
    h2,w2=list(map(int,input().split()))
    b=[]
    for _ in range(h2):
        row=list(map(int,input().split()))
        b.append(row)
    return h1,w1,a,h2,w2,b

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
                    exit()
    print('No')

=======
Suggestion 8

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
            flg = True
            for k in range(h2):
                for l in range(w2):
                    if a[i + k][j + l] != b[k][l]:
                        flg = False
            if flg:
                print('Yes')
                return
    print('No')

=======
Suggestion 9

def main():
    h1, w1 = map(int, input().split())
    a = [[0 for i in range(w1)] for j in range(h1)]
    for i in range(h1):
        a[i] = list(map(int, input().split()))
    h2, w2 = map(int, input().split())
    b = [[0 for i in range(w2)] for j in range(h2)]
    for i in range(h2):
        b[i] = list(map(int, input().split()))

    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if a[i][j] == b[0][0]:
                if a[i:i + h2] == b:
                    print("Yes")
                    return

    print("No")

=======
Suggestion 10

def main():
    # Get input here
    h1, w1 = map(int, input().strip().split())
    a = []
    for _ in range(h1):
        a.append(list(map(int, input().strip().split())))
    h2, w2 = map(int, input().strip().split())
    b = []
    for _ in range(h2):
        b.append(list(map(int, input().strip().split())))
    # print(h1, w1, a)
    # print(h2, w2, b)
    # Main logic starts here
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # print(i, j)
            if a[i][j] == b[0][0]:
                flag = 1
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = 0
                            break
                    if flag == 0:
                        break
                if flag == 1:
                    print("Yes")
                    return
    print("No")
