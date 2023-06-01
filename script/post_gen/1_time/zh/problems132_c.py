Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    n = int(input())
    d = list(map(int, input().split()))
    # 排序
    d.sort()
    # 找到中位数
    if n%2 == 0:
        k = (d[int(n/2)-1] + d[int(n/2)])/2
    else:
        k = d[int((n-1)/2)]
    # 找到中位数后面第一个不等于中位数的数字
    i = 0
    while d[int(n/2)+i] == k:
        i += 1
    # 计算答案
    print(i)

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2] - d[n//2-1])

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d = sorted(d)
    print(d[n//2] - d[n//2-1])

=======
Suggestion 4

def f(k):
    arc = 0
    abc = 0
    for i in range(n):
        if a[i] >= k:
            arc += 1
        else:
            abc += 1
    if arc == abc:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))

l = 0
r = max(a)+1
while r - l > 1:
    m = (l + r) // 2
    if f(m):
        l = m
    else:
        r = m
print(l)

=======
Suggestion 5

def main():
    n = int(input())
    d_list = [int(i) for i in input().split()]
    d_list.sort()
    #print(d_list)
    #print(d_list[n//2])
    print(d_list[n//2]-d_list[n//2-1])

=======
Suggestion 6

def get_input():
    n = int(input())
    ds = list(map(int, input().split()))
    return n, ds

=======
Suggestion 7

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    d.sort()
    if n % 2 == 0:
        print(d[n//2] - d[n//2-1])
    else:
        print(0)

=======
Suggestion 8

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if N%2 == 0:
        print(d[int(N/2)] - d[int(N/2)-1])
    else:
        print(0)

=======
Suggestion 9

def main():
    n = int(input())
    ds = list(map(int, input().split()))
    ds.sort()
    #print(ds)
    left = ds[n//2-1]
    right = ds[n//2]
    print(right-left)

=======
Suggestion 10

def main():
    # 读取输入
    N = int(input())
    d = list(map(int, input().split()))

    # 求和
    s = sum(d)

    # 累积和
    a = [0] * (N + 1)
    for i in range(N):
        a[i + 1] = a[i] + d[i]

    # 确定最小值
    m = 10**9
    for i in range(1, N + 1):
        m = min(m, abs(s - 2 * a[i]))

    # 计数
    ans = 0
    for i in range(1, N + 1):
        if abs(s - 2 * a[i]) == m:
            ans += 1

    # 输出
    print(ans)
