Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(input()))
    for i in range(w):
        c = 0
        for j in range(h):
            if a[j][i] == '#':
                c += 1
        print(c)

=======
Suggestion 2

def problems274_b():
    H,W = map(int,input().split())
    list = []
    for i in range(H):
        list.append(input())
    for i in range(W):
        count = 0
        for j in range(H):
            if list[j][i] == '#':
                count += 1
        print(count,end=' ')
    return

=======
Suggestion 3

def problems274_b():
    pass

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == "#":
                x += 1
        print(x)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    #print(h, w)
    data = [0 for i in range(w)]
    #print(data)
    for i in range(h):
        row = input()
        #print(row)
        for j in range(w):
            #print(row[j])
            if row[j] == '#':
                data[j] += 1
    #print(data)
    for i in range(w):
        print(data[i], end=' ')
    print()

=======
Suggestion 6

def get_input():
    h, w = map(int, input().split())
    input_list = []
    for i in range(h):
        input_list.append(input())
    return h, w, input_list

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        c = 0
        for j in range(h):
            if a[j][i] == "#":
                c += 1
        print(c)

=======
Suggestion 8

def count_box(box):
    box_count = 0
    for i in range(len(box)):
        if box[i] == '#':
            box_count += 1
    return box_count

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in ans:
        print(''.join(i))
