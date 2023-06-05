Synthesizing 10/10 solutions

=======
Suggestion 1

def count_min_blocks(H, W, A):
    # 数组A中的最小值
    min_num = min([min(a) for a in A])
    # 数组A中的最大值
    max_num = max([max(a) for a in A])
    # 最小值和最大值之间的差值
    diff = max_num - min_num
    # 最小值和最大值之间的差值的最小值
    min_diff = diff
    # 最小值和最大值之间的差值的最小值的最小值
    min_min_diff = min_diff
    # 最小值和最大值之间的差值的最小值的最小值的最小值
    min_min_min_diff = min_min_diff
    # 最小值和最大值之间的差值的最小值的最小值的最小值的最小值
    min_min_min_min_diff = min_min_min_diff
    # 最小值和最大值之间的差值的最小值的最小值的最小值的最小值的最小值
    min_min_min_min_min_diff = min_min_min_min_diff
    # 最小值和最大值之间的差值的最小值的最小值的最小值的最小值的最小值的最小值
    min_min_min_min_min_min_diff = min_min_min_min_min_diff
    # 最小值和最大值之间的差值的最小值的最小值的最小值的最小值的最小值的最小值的最小值
    min_min_min_min_min_min_min_diff = min_min_min_min_min_min_diff
    # 最小值和最大值之间的��

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    total = sum(map(sum, A))
    ave = total // (H * W)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += abs(A[i][j] - ave)
    print(ans // 2)

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_v = 101
    for i in range(h):
        for j in range(w):
            min_v = min(a[i][j],min_v)
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_v
    print(ans)

=======
Suggestion 4

def get_min_block(H, W, A):
    min_block = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_block:
                min_block = A[i][j]
    return min_block

=======
Suggestion 5

def main():
    #读取输入
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    #求出所有的图块数
    total = sum(map(sum, a))
    #如果不能整除，就不能使所有方格都有相同数量的图块，输出NO
    if total % (h * w) != 0:
        print("NO")
        return
    #求出每个方格都有多少个图块
    ave = total // (h * w)
    #求出需要移除的图块数
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += abs(a[i][j] - ave)
    print(ans // 2)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_a = a[0][0]
    for i in range(h):
        for j in range(w):
            if min_a > a[i][j]:
                min_a = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(a) for a in A])
    print(sum([sum(a) for a in A]) - min_A * H * W)

=======
Suggestion 8

def problems186_b():
    print("")

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = min(map(min, A))
    print(sum(map(lambda x: sum(map(lambda y: y - min_num, x)), A)))

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    minA = 101
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)
