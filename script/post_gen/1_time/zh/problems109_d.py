Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j != W-1:
                    a[i][j] -= 1
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i != H-1:
                    a[i][j] -= 1
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 3

def printList(l):
    print(' '.join(map(str, l)))

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W - 1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
    for i in range(H - 1):
        if a[i][W - 1] % 2 == 1:
            a[i][W - 1] -= 1
            a[i + 1][W - 1] += 1
            ans.append((i + 1, W, i + 2, W))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

solve()

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w-1):
            if a[i][j]%2==1:
                a[i][j+1]+=1
                ans.append((i+1,j+1,i+1,j+2))
    for i in range(h-1):
        if a[i][w-1]%2==1:
            a[i+1][w-1]+=1
            ans.append((i+1,w,i+2,w))
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])

=======
Suggestion 7

def printList(l):
    for i in l:
        print(i)
