Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s, t = input().split()
    if s < t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s,t = input().split()
    if s < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S, T = input().split()
    if S < T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def compare_str(a,b):
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
    return False

=======
Suggestion 5

def main():
    a,b = input().split()
    if a < b:
        print('Yes')
    else:
        print('No')
    return 0

=======
Suggestion 6

def main():
    s, t = input().split()
    if s < t:
        print("Yes")
    else:
        print("No")
    return 0

=======
Suggestion 7

def main():
    # 读取输入
    s, t = input().split()
    # 在这里编写处理
    if s < t:
        print("Yes")
    else:
        print("No")
    # 输出结果
    #print(s, t)
    pass
