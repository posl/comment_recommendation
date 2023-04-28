Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    ans = []
    for i in range(H):
        if '#' in a[i]:
            ans.append(a[i])
    ans = [[ans[j][i] for j in range(len(ans))] for i in range(len(ans[0]))]
    for i in range(len(ans)):
        print(''.join(ans[i]))

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    b = []
    for i in range(h):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b)):
        if not '.' in b[i]:
            c.append(i)
    d = []
    for i in range(w):
        if not '.' in [b[j][i] for j in range(len(b))]:
            d.append(i)
    for i in range(len(b)):
        e = ''
        for j in range(w):
            if not j in d:
                e += b[i][j]
        print(e)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    ans = []
    for i in range(h):
        if a[i].count('.') != w:
            ans.append(a[i])
    ans = list(map(list, zip(*ans)))
    for i in range(len(ans)):
        print(''.join(ans[i]))

=======
Suggestion 4

def get_input():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    return h, w, a

=======
Suggestion 5

def problems107_b():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    for i in range(H):
        if a[i].count('.') == W:
            a[i] = []
    for j in range(W):
        if [a[i][j] for i in range(H)].count('.') == H:
            for i in range(H):
                a[i][j] = ''
    for i in range(H):
        if a[i]:
            print(''.join(a[i]))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    for i in range(h):
        if a[i].count('.') == w:
            for j in range(w):
                a[i][j] = ''
    for j in range(w):
        if [a[i][j] for i in range(h)].count('') == h:
            for i in range(h):
                a[i][j] = ''
    for i in range(h):
        if a[i].count('') == w:
            continue
        else:
            print(''.join(a[i]))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())

    b = []
    for i in range(H):
        if a[i].count('#') != 0:
            b.append(a[i])

    c = []
    for i in range(len(b[0])):
        if [j[i] for j in b].count('#') != 0:
            c.append([j[i] for j in b])

    d = []
    for i in range(len(c[0])):
        d.append(''.join([j[i] for j in c]))

    for i in d:
        print(i)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [input() for i in range(h)]
    b = []
    for i in range(h):
        if not all(j == "." for j in a[i]):
            b.append(a[i])
    c = []
    for i in range(w):
        if not all(j == "." for j in [a[j][i] for j in range(h)]):
            c.append([a[j][i] for j in range(h)])
    for i in range(len(b)):
        print("".join(b[i]))
    print()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    #print(H, W)
    a = []
    for i in range(H):
        a.append(input())
    #print(a)
    for i in range(len(a)):
        if a[i] == "." * W:
            a[i] = ""
    #print(a)
    b = []
    for i in range(W):
        b.append("")
    #print(b)
    for i in range(H):
        for j in range(W):
            b[j] += a[i][j]
    #print(b)
    for i in range(len(b)):
        if b[i] == "." * H:
            b[i] = ""
    #print(b)
    c = []
    for i in range(len(b)):
        if b[i] != "":
            c.append(b[i])
    #print(c)
    for i in range(len(c)):
        print(c[i])

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    #print(a)

    h_list = [False] * h
    w_list = [False] * w

    #print(h_list)
    #print(w_list)

    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                h_list[i] = True
                w_list[j] = True

    #print(h_list)
    #print(w_list)

    for i in range(h):
        if h_list[i]:
            for j in range(w):
                if w_list[j]:
                    print(a[i][j], end='')
            print()
