Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    #print(H,W)
    grid = [input() for _ in range(H)]
    #print(grid)
    for i in range(H):
        print(grid[i].count('#'))

=======
Suggestion 2

def get_input():
    h,w = map(int,input().split())
    x = []
    for i in range(h):
        x.append(list(input()))
    return h,w,x

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        print(count, end=' ')
    print()
main()

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c[i][j] = 1 if c[i][j] == '#' else 0
    for i in range(h):
        for j in range(1, w):
            c[i][j] += c[i][j-1]
    for j in range(w):
        for i in range(1, h):
            c[i][j] += c[i-1][j]
    for i in range(h):
        print(' '.join(map(str, c[i])))

main()

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    l = []
    for i in range(h):
        l.append(list(input()))
    for i in range(w):
        x = 0
        for j in range(h):
            if l[j][i] == "#":
                x += 1
        print(x,end=" ")

=======
Suggestion 6

def problems274_b():
    h,w = map(int,input().split())
    box = []
    for i in range(h):
        box.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if box[j][i] == "#":
                count += 1
        print(count,end=" ")
    print()

=======
Suggestion 7

def f(n, m, a):
    b = []
    for j in range(m):
        count = 0
        for i in range(n):
            if a[i][j] == '#':
                count += 1
        b.append(count)
    return b

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(input()))

b = f(n, m, a)
print(*b)

=======
Suggestion 8

def solve(h, w, c):
    ans = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = 1
    for i in range(h):
        for j in range(1, w):
            ans[i][j] += ans[i][j-1]
    for i in range(1, h):
        for j in range(w):
            ans[i][j] += ans[i-1][j]
    return ans

=======
Suggestion 9

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if a[j][i] == '#':
                count += 1
        print(count, end=' ')
    print()

=======
Suggestion 10

def main():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    ans = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if ans[i][j] == '#':
                if i-1 >= 0:
                    if ans[i-1][j] != '#':
                        ans[i-1][j] += 1
                if i+1 < h:
                    if ans[i+1][j] != '#':
                        ans[i+1][j] += 1
                if j-1 >= 0:
                    if ans[i][j-1] != '#':
                        ans[i][j-1] += 1
                if j+1 < w:
                    if ans[i][j+1] != '#':
                        ans[i][j+1] += 1
                if i-1 >= 0 and j-1 >= 0:
                    if ans[i-1][j-1] != '#':
                        ans[i-1][j-1] += 1
                if i-1 >= 0 and j+1 < w:
                    if ans[i-1][j+1] != '#':
                        ans[i-1][j+1] += 1
                if i+1 < h and j-1 >= 0:
                    if ans[i+1][j-1] != '#':
                        ans[i+1][j-1] += 1
                if i+1 < h and j+1 < w:
                    if ans[i+1][j+1] != '#':
                        ans[i+1][j+1] += 1
    for i in range(h):
        for j in range(w):
            if ans[i][j] == '#':
                print('#',end='')
            else:
                print(ans[i][j],end='')
        print()
