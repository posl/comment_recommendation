Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num(num):
    count = 0
    for i in range(len(num)):
        if num[i] == '#':
            count += 1
    return count

H, W = map(int, input().split())
num = []
for i in range(H):
    num.append(input())

for i in range(W):
    print(get_num([num[j][i] for j in range(H)]), end=' ')
print()

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        s = 0
        for j in range(h):
            if a[j][i] == "#":
                s += 1
        print(s)

=======
Suggestion 3

def problem274_b():
    #输入
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    #处理
    for i in range(H):
        count = 0
        for j in range(W):
            if C[i][j] == '#':
                count += 1
        print(count)

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                ans[i][j] = "#"
    for i in range(H):
        print("".join(ans[i]))

=======
Suggestion 5

def get_x_list(h, w, c_list):
    x_list = []
    for j in range(w):
        x = 0
        for i in range(h):
            if c_list[i][j] == '#':
                x += 1
        x_list.append(x)
    return x_list

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    C = [input() for i in range(H)]
    ans = []
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == '#':
                count += 1
        ans.append(count)
    print(*ans)

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    c = [input() for i in range(h)]
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == '#':
                x += 1
        print(x,end=' ')
    print()

=======
Suggestion 8

def problems274_b():
    h,w = input().split()
    h = int(h)
    w = int(w)
    l = []
    for i in range(h):
        l.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if l[i][j] == '#':
                count = count + 1
        print(count,end=' ')
    print()

=======
Suggestion 9

def problem274_b():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(W):
        X = 0
        for j in range(H):
            if C[j][i] == "#":
                X += 1
        print(X, end=" ")
    print("")

=======
Suggestion 10

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except:
            break
    return input_list
