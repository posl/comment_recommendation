Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2]-a[0])

=======
Suggestion 2

def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())

    # 请在此处编写您的代码
    # 请注意，您可以添加其他函数，而不仅仅是main（）。

    # 请不要修改以下内容。
    print(0)

=======
Suggestion 3

def main():
    a1, a2, a3 = map(int, input().split())
    print(min(abs(a2-a1)+abs(a3-a2), abs(a3-a1)+abs(a2-a3), abs(a1-a2)+abs(a3-a1)))
    return

=======
Suggestion 4

def get_min_cost(a1, a2, a3):
    a = [a1, a2, a3]
    a.sort()
    return a[2] - a[0]

=======
Suggestion 5

def solve(a):
    a.sort()
    return a[2]-a[0]

=======
Suggestion 6

def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    print(a[2]-a[0])

main()

=======
Suggestion 7

def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 请在此处编写您的代码（可选）
    # 输出结果
    print(min(abs(a1-a2)+abs(a2-a3),abs(a1-a3)+abs(a2-a3),abs(a1-a2)+abs(a1-a3)))
