Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print('No')
                        return
    print('Yes')

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print("No")
                        return
    print("Yes")

=======
Suggestion 3

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            for k in range(i+1, h):
                for l in range(j+1, w):
                    if a[i][j] + a[k][l] > a[i][l] + a[k][j]:
                        print("No")
                        return
    print("Yes")

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(i+1,h):
                for l in range(j+1,w):
                    if a[i][j] + a[k][l] > a[i][l] + a[k][j]:
                        print("No")
                        return
    print("Yes")

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    for i in range(h-1):
        for j in range(w-1):
            if a[i][j] + a[i+1][j+1] > a[i+1][j] + a[i][j+1]:
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            for k in range(i+1, h):
                for l in range(j+1, w):
                    if a[i][j] + a[k][l] > a[i][l] + a[k][j]:
                        print('No')
                        exit()
    print('Yes')

main()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    print("Yes" if all(A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2] for i1 in range(H) for i2 in range(i1 + 1, H) for j1 in range(W) for j2 in range(j1 + 1, W)) else "No")

=======
Suggestion 8

def check_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(i+1, len(grid)):
                for l in range(j+1, len(grid[0])):
                    if(grid[i][j]+grid[k][l] > grid[i][l]+grid[k][j]):
                        return False
    return True

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    #print(A)

    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print("No")
                        exit()
    print("Yes")

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    return "Yes" if all(A[i][j] + A[i+1][j+1] <= A[i+1][j] + A[i][j+1] for i in range(H-1) for j in range(W-1)) else "No"

print(solve())
