Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j]
    print(ans - H * W)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(row) for row in a])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    minA = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < minA:
                minA = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [j for i in A for j in i]
    A.sort()
    ans = 0
    for i in range(len(A)):
        ans += abs(A[i] - A[len(A)//2])
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    print(sum([sum(x) for x in a]) - min([min(x) for x in a]) * h * w)

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    minA = min([min(a) for a in A])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [item for sublist in A for item in sublist]
    print(sum([abs(i - sum(A) / (H * W)) for i in A]) // 2)

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    ans = 10**9
    for i in range(101):
        cnt = 0
        for j in range(H):
            for k in range(W):
                if A[j][k] > i:
                    cnt += A[j][k] - i
        ans = min(ans,cnt)
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #print(A)
    #print(H)
    #print(W)
    #print(A)
    #print(len(A))
    #print(len(A[0]))
    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[2][2])
    #print(A[0])
    #print(A[1])
    #print(A[2])
    
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    
    #print

=======
Suggestion 10

def main():
    #H: number of rows
    #W: number of columns
    #A: number of blocks in each square
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    #count: count of each number of blocks
    count = [0] * 101

    #count the number of blocks in each square
    for i in range(H):
        for j in range(W):
            count[A[i][j]] += 1

    #ans: the minimum number of blocks that must be removed
    ans = 10**6

    #try each number of blocks
    for i in range(101):
        #blocks: number of blocks to be removed
        #num: number of squares with i blocks
        blocks = 0
        num = 0
        for j in range(101):
            #if number of blocks is j, remove (j-i) blocks from each square
            if j > i:
                blocks += (j-i) * count[j]
            #if number of blocks is j, add j blocks to each square
            else:
                num += count[j]
        #if the number of blocks is i, the number of blocks to be removed is blocks
        if num == H * W:
            ans = min(ans, blocks)

    print(ans)
