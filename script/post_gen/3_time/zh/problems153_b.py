Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def f(h, n, a):
    a.sort()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            return "Yes"
    return "No"

h, n = map(int, input().split())
a = list(map(int, input().split()))
print(f(h, n, a))

=======
Suggestion 4

def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 解决问题
    # 用一个布尔数组来记录是否已经使用过某个招数
    used = [False] * (H + 1)
    # 用一个变量来记录当前的健康值
    health = H
    # 用一个变量来记录当前的招数序号
    i = 0
    while True:
        # 如果当前的招数序号超过了招数种类的最大值，那么就说明
        # 无法再继续战斗了（健康值不会再减少了），所以判断
        # 健康值是否已经降到了0以下，如果是则返回Yes，否则
        # 返回No
        if i >= N:
            return "Yes" if health <= 0 else "No"
        # 如果当前的健康值已经降到了0以下，那么说明已经赢得了
        # 战斗，所以返回Yes
        if health <= 0:
            return "Yes"
        # 如果当前的健康值已经降到了0以上，但是招数已经用完了
        # 那么说明已经输掉了战斗，所以返回No
        if i >= N:
            return "No"
        # 如果当前的健康值还大于0，且招数还没有用完，那么就
        # 选择一个招数来使用，如果这个招数已经使用过了，那么
        # 就换一个招数来使用，直到找到一个没有使用过的招数
        while used[i]:
            i += 1
        # 使用招数i
        health -= A[i]
        # 记录招数i已经使用过了
        used[i] = True

=======
Suggestion 5

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if h <= sum(a) else 'No')

=======
Suggestion 6

def solve():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) >= H:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 一开始的健康值
    health = H
    # 一开始的最小健康值
    min_health = health
    # 循环N次
    for i in range(N):
        # 健康值减少
        health -= A[i]
        # 如果健康值小于最小健康值
        if health < min_health:
            # 更新最小健康值
            min_health = health
    # 如果最小健康值小于等于0
    if min_health <= 0:
        # 打印Yes
        print('Yes')
    # 否则
    else:
        # 打印No
        print('No')

=======
Suggestion 8

def problem153_b():
    pass

=======
Suggestion 9

def main():
    H,N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print('Yes')
    else:
        print('No')
