Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        if '#' in [b[j][i] for j in range(len(b))]:
            c.append([b[j][i] for j in range(len(b))])
    for i in range(len(c)):
        print(''.join(c[i]))

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if "#" in a[i]:
            b.append(a[i])
    c = [list(x) for x in zip(*b)]
    d = []
    for i in range(w):
        if "#" in c[i]:
            d.append(c[i])
    e = [list(x) for x in zip(*d)]
    for i in range(len(e)):
        print("".join(e[i]))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if a[i].count('.') != w:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        if ''.join([b[j][i] for j in range(len(b))]).count('.') != len(b):
            c.append(''.join([b[j][i] for j in range(len(b))]))
    for i in range(len(c)):
        print(c[i])

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if a[i].count(".") != w:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        for j in range(len(b)):
            if b[j][i] == "#":
                break
        else:
            c.append(i)
    for i in range(len(b)):
        for j in range(len(c)):
            b[i] = b[i][:c[j]] + b[i][c[j]+1:]
    for i in range(len(b)):
        print(b[i])
    return 0

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(h):
        if a[i].count(".") == w:
            a[i] = ""
    for i in range(w):
        count = 0
        for j in range(h):
            if a[j] != "":
                if a[j][i] == ".":
                    count += 1
        if count == h:
            for j in range(h):
                a[j] = a[j][:i] + a[j][i+1:]
    for i in range(h):
        if a[i] != "":
            print(a[i])

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    a = [row for row in a if '#' in row]
    a = list(zip(*[row for row in zip(*a) if '#' in row]))
    print('\n'.join(''.join(row) for row in a))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    r = []
    c = []
    for i in range(H):
        if a[i].count(".") == W:
            r.append(i)
    for i in range(W):
        if [a[j][i] for j in range(H)].count(".") == H:
            c.append(i)
    for i in range(H):
        if not i in r:
            print("".join([a[i][j] for j in range(W) if not j in c]))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    a = [a[i] for i in range(h) if '#' in a[i]]
    a = [list(a[i]) for i in range(len(a)) if '#' in a[i]]
    for i in range(len(a)):
        print(''.join(a[i]))

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    #print(a)
    #print(H, W)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[0][3])
    #print(a[0][4])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[1][3])
    #print(a[1][4])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[2][3])
    #print(a[2][4])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[3][3])
    #print(a[3][4])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[4][3])
    #print(a[4][4])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[5][3])
    #print(a[5][4])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[6][3])
    #print(a[6][4])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[7][3])
    #print(a[7][4])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #print(a[8][3])
    #print(a[8][4])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[9][2])
    #print(a[9][3])
    #print(a[9][4])
    #print(a[10][0])
    #print

=======
Suggestion 10

def problem107_b():
    H, W = map(int, input().split())
    a = []
    for _ in range(H):
        a.append(input())
    print(a)
