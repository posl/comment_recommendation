Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    rows = [False]*h
    cols = [False]*w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                rows[i] = True
                cols[j] = True
    for i in range(h):
        if rows[i]:
            for j in range(w):
                if cols[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if "#" in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        d = ""
        for j in range(len(b)):
            d += b[j][i]
        if "#" in d:
            c.append(d)
    for i in range(len(c)):
        print(c[i])

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = []
    for i in range(H):
        if "#" in A[i]:
            B.append(A[i])
    C = []
    for i in range(len(B[0])):
        flag = True
        for j in range(len(B)):
            if B[j][i] == "#":
                flag = False
                break
        if flag:
            C.append(i)
    for i in range(len(B)):
        for j in range(len(C)):
            del B[i][C[j]-j]
    for i in range(len(B)):
        print("".join(B[i]))

main()

=======
Suggestion 4

def main():
    hw = input().split()
    h = int(hw[0])
    w = int(hw[1])
    a = []
    for i in range(h):
        a.append(input())
    ans = []
    for i in range(h):
        if a[i].count('.') != w:
            ans.append(a[i])
    ans2 = []
    for j in range(w):
        tmp = 0
        for i in range(len(ans)):
            if ans[i][j] == '.':
                tmp += 1
        if tmp != len(ans):
            ans2.append(j)
    for i in range(len(ans)):
        for j in ans2:
            print(ans[i][j], end='')
        print()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    ans = []
    for i in range(H):
        if a[i].count("#") > 0:
            ans.append(a[i])
    ans2 = []
    for i in range(len(ans[0])):
        cnt = 0
        for j in range(len(ans)):
            if ans[j][i] == "#":
                cnt += 1
        if cnt > 0:
            ans2.append(i)
    for i in range(len(ans)):
        for j in range(len(ans2)):
            print(ans[i][ans2[j]], end="")
        print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    Hlist = []
    Wlist = []
    for i in range(H):
        if '#' not in a[i]:
            Hlist.append(i)
    for j in range(W):
        if '#' not in [a[i][j] for i in range(H)]:
            Wlist.append(j)
    for i in range(H):
        if i not in Hlist:
            print(''.join([a[i][j] for j in range(W) if j not in Wlist]))
    return

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if not all(a[i][j] == "." for j in range(w)):
            b.append(a[i])
    c = []
    for j in range(w):
        if not all(a[i][j] == "." for i in range(h)):
            c.append(j)
    for i in range(len(b)):
        for j in c:
            print(b[i][j],end="")
        print()

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    #print(H, W)
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])

    for i in range(H):
        if a[i] == '.' * W:
            continue
        else:
            for j in range(W):
                if a[i][j] == '#':
                    break
                else:
                    print(a[i][j], end='')
            print()
    #print(a[0][0], a[0][1], a[0][2], a[0][3])
    #print(a[1][0], a[1][1], a[1][2], a[1][3])
    #print(a[2][0], a[2][1], a[2][2], a[2][3])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    a = [x for x in a if x != ['.'] * W]
    a = [x for x in zip(*a) if x != ['.'] * len(a)]
    a = [list(x) for x in zip(*a)]
    for x in a:
        print(''.join(x))

=======
Suggestion 10

def problems107_b():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(input())
    matrix = list(filter(lambda x: '#' in x, matrix))
    matrix = list(zip(*matrix))
    matrix = list(filter(lambda x: '#' in x, matrix))
    matrix = list(zip(*matrix))
    for i in matrix:
        print(''.join(i))
