Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(i) for i in a])
    print(sum([sum(i) for i in a]) - h * w * min_a)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = min(map(min, A))
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_num
    print(ans)

=======
Suggestion 3

def main():
    # 读取输入
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 计算平均值
    average = sum(sum(A, [])) // (H * W)

    # 计算答案
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += abs(A[i][j] - average)

    # 输出答案
    print(ans)

=======
Suggestion 4

def get_min_blocks(H, W, A):
    #最小块数
    min_blocks = 0
    #求和
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j]
    #求平均数
    average = sum / (H * W)
    #求最小块数
    for i in range(H):
        for j in range(W):
            if average < A[i][j]:
                min_blocks += A[i][j] - average
    return min_blocks

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    min_a = min([min(i) for i in a])
    print(sum([sum(i) for i in a]) - min_a * h * w)

=======
Suggestion 6

def solve(h, w, a):
    min_a = min([min(row) for row in a])
    return sum([sum([a[i][j] - min_a for j in range(w)]) for i in range(h)])

=======
Suggestion 7

def cal_min_block_num(H,W,block_list):
    min_block_num = 10000
    for i in range(H):
        for j in range(W):
            if block_list[i][j] < min_block_num:
                min_block_num = block_list[i][j]
    return min_block_num

=======
Suggestion 8

def move_block(H,W,A):
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算当前的总块数
    sum_block = 0
    for i in range(H):
        for j in range(W):
            sum_block += A[i][j]
    #计算平均每个格子应该有的块数
    ave_block = sum_block//(H*W)
    #计算需要移动的块数
    move_block = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > ave_block:
                move_block += A[i][j] - ave_block
    return move_block

=======
Suggestion 9

def solve():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))
    min_num = 100
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_num:
                min_num = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_num
    print(ans)

solve()

=======
Suggestion 10

def problems186_b():
    pass
