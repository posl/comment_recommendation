Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #S = input()
    S = "+-++"
    print(S.count('+')-S.count('-'))

=======
Suggestion 2

def main():
    S = input()
    #print(S)
    count = 0
    for i in range(len(S)):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 4

def main():
    # 读取输入
    S = input()

    # 计算结果
    result = 0
    for i in range(4):
        if S[i] == '+':
            result += 1
        else:
            result -= 1

    # 打印结果
    print(result)

=======
Suggestion 5

def main():
    # 输入字符串
    s = input()
    # 计算结果
    result = 0
    # 遍历字符串
    for i in range(0, len(s)):
        # 如果是+号，结果+1
        if s[i] == '+':
            result += 1
        # 如果是-号，结果-1
        else:
            result -= 1
    # 输出结果
    print(result)

=======
Suggestion 6

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 7

def main():
    #读入数据
    s = input()
    #print(s)
    #计算结果
    result = 0
    for i in range(0,4):
        if s[i] == "+":
            result += 1
        else:
            result -= 1
    #输出结果
    print(result)

=======
Suggestion 8

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 9

def main():
    S = input()
    count = 0
    for i in S:
        if i == "+":
            count += 1
        elif i == "-":
            count -= 1
    print(count)

=======
Suggestion 10

def get_result(s):
    result = 0
    for i in s:
        if i == '+':
            result += 1
        else:
            result -= 1
    return result
