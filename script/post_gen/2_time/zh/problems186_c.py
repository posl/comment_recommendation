Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_v = min([min(a) for a in A])
    print(sum([sum([a - min_v for a in a]) for a in A]))

=======
Suggestion 2

def remove_blocks(h, w, blocks):
    # 1. 求出所有块的总数
    blocks_sum = 0
    for row in blocks:
        blocks_sum += sum(row)
    # 2. 求出每个块的平均数
    blocks_avg = blocks_sum // (h * w)
    # 3. 求出所有块的差值
    blocks_diff = 0
    for row in blocks:
        for block in row:
            blocks_diff += abs(block - blocks_avg)
    # 4. 求出所有块的差值之和
    return blocks_diff

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = min([min(A[i]) for i in range(H)])
    print(sum([sum([A[i][j] - min_A for j in range(W)]) for i in range(H)]))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    a = [[int(i) for i in input().split()] for i in range(H)]
    min_a = 100
    for i in range(H):
        for j in range(W):
            if a[i][j] < min_a:
                min_a = a[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_A = min([min(i) for i in A])
    print(sum([sum([i - min_A for i in j]) for j in A]))

=======
Suggestion 6

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_num = min([min(a) for a in A])
    ans = 0
    for a in A:
        for i in a:
            ans += i - min_num
    print(ans)

=======
Suggestion 7

def readinput():
    H,W=list(map(int,input().split()))
    A=[]
    for i in range(H):
        A.append(list(map(int,input().split())))
    return H,W,A

=======
Suggestion 8

def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = min([min(a) for a in A])

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    minA = min([min(a) for a in A])

    print(sum([sum([a - minA for a in a]) for a in A]))

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = 100
    for i in range(H):
        for j in range(W):
            min_num = min(min_num, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_num
    print(ans)
solve()
