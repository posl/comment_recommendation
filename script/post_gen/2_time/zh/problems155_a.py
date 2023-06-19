Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c or a == c and b != c or b == c and a != c:
        print("是")
    else:
        print("否")

=======
Suggestion 3

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理
    if a == b and a != c:
        print("是")
    elif a == c and a != b:
        print("是")
    elif b == c and b != a:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and c != b:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    if a[0] == a[1] and a[1] != a[2]:
        print("Yes")
    elif a[0] != a[1] and a[1] == a[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 逻辑处理
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_diff(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:
        return False

a, b, c = map(int, input().split())

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("是")
    elif b == c and c != a:
        print("是")
    elif c == a and a != b:
        print("是")
    else:
        print("否")

=======
Suggestion 9

def main():
    # 读取输入
    nums = input().split(' ')
    # 判断三个数是否相等
    if nums[0] == nums[1] == nums[2]:
        print('否')
    # 判断两个数是否相等
    elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
        print('是')
    else:
        print('否')

=======
Suggestion 10

def main():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    else:
        print("No")
