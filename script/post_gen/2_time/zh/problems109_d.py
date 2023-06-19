Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solution(H,W,coins):
    N = 0
    operation = []
    for i in range(H):
        for j in range(W):
            if coins[i][j] % 2 == 1:
                if j < W - 1:
                    coins[i][j] -= 1
                    coins[i][j+1] += 1
                    N += 1
                    operation.append([i+1,j+1,i+1,j+2])
                elif i < H - 1:
                    coins[i][j] -= 1
                    coins[i+1][j] += 1
                    N += 1
                    operation.append([i+1,j+1,i+2,j+1])
    print(N)
    for i in range(N):
        print(operation[i][0], operation[i][1], operation[i][2], operation[i][3])

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    a = [[int(i) for i in input().split()] for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j]%2 == 1:
                if j != w-1:
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i != h-1:
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 4

def solve():
    H,W = map(int,input().split())
    a = []
    for i in range(H):
        a.append(list(map(int,input().split())))

    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i < H - 1:
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])

solve()

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j < w - 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < h - 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======
Suggestion 6

def print_list(l):
    for i in l:
        print(i)

=======
Suggestion 7

def solve(h,w,coins):
    #先将偶数的单元格填满
    ans=[]
    for i in range(h):
        for j in range(w):
            if coins[i][j]%2==1:
                if j<w-1:
                    coins[i][j+1]+=1
                    ans.append((i+1,j+1,i+1,j+2))
                elif i<h-1:
                    coins[i+1][j]+=1
                    ans.append((i+1,j+1,i+2,j+1))
    #再将奇数的单元格填满
    for i in range(h):
        for j in range(w):
            while coins[i][j]%2==1:
                if j<w-1:
                    coins[i][j+1]+=1
                    ans.append((i+1,j+1,i+1,j+2))
                elif i<h-1:
                    coins[i+1][j]+=1
                    ans.append((i+1,j+1,i+2,j+1))
    return ans

=======
Suggestion 8

def solve(h, w, a):
    ans = []
    for i in range(h):
        for j in range(w-1):
            if a[i][j] % 2 == 1:
                a[i][j+1] += 1
                ans.append((i+1, j+1, i+1, j+2))
    for i in range(h-1):
        if a[i][w-1] % 2 == 1:
            a[i+1][w-1] += 1
            ans.append((i+1, w, i+2, w))
    print(len(ans))
    for i in ans:
        print(*i)
