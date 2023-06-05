Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_min_cost(a1, a2, a3):
    cost = 0
    if a1 > a2:
        cost += a1 - a2
        a1 = a2
    if a1 > a3:
        cost += a1 - a3
        a1 = a3
    if a2 < a1:
        cost += a2 - a1
        a2 = a1
    if a2 > a3:
        cost += a2 - a3
        a2 = a3
    return cost

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 3

def main():
    # 读取输入
    a1,a2,a3 = map(int, input().split())
    # 用一个list保存
    a = [a1, a2, a3]
    # 从小到大排序
    a.sort()
    # 从小到大排序后，a[0]一定是最小的，所以，a[1]和a[2]的差值一定是最小的
    # 所以，完成所有任务的最小成本就是a[2]-a[0]
    print(a[2]-a[0])

=======
Suggestion 4

def main():
    #输入
    a1,a2,a3 = map(int,input().split())
    #处理
    #输出
    print(max(a1,a2,a3)-min(a1,a2,a3))

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 6

def main():
    # 从标准输入读取
    a1, a2, a3 = map(int, input().split())
    # 请在此处编写您的代码
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。
    # 请注意，如果使用了标准输入，则不要使用input（）。
    # 请注意，如果使用了标准输出，则不要使用print（）。

    # 从标准输出打印
    print(ans)

=======
Suggestion 7

def main():
    # 读取数据
    a1, a2, a3 = map(int, input().split())

    # 计算结果
    result = 0
    if a1 > a2:
        result += a1 - a2
        a1 = a2
    if a1 > a3:
        result += a1 - a3
        a1 = a3
    if a2 < a3:
        result += a3 - a2
        a3 = a2
    if a1 < a2:
        result += a2 - a1
        a2 = a1
    if a1 < a3:
        result += a3 - a1
        a3 = a1
    if a2 > a3:
        result += a2 - a3
        a2 = a3

    # 输出结果
    print(result)
