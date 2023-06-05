Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    # 依次处理t中的字符
    result = ""
    for c in t:
        if c == "1":
            result += s1
        elif c == "2":
            result += s2
        elif c == "3":
            result += s3

    # 打印结果
    print(result)

=======
Suggestion 2

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    result = ""
    for t in T:
        if t == "1":
            result += S_1
        elif t == "2":
            result += S_2
        else:
            result += S_3
    print(result)

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in range(len(T)):
        if T[i] == '1':
            print(S1, end='')
        elif T[i] == '2':
            print(S2, end='')
        else:
            print(S3, end='')
    print()

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in t:
        if i == '1':
            print(s1, end='')
        elif i == '2':
            print(s2, end='')
        else:
            print(s3, end='')
    print()

=======
Suggestion 5

def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    T = input()

    # 处理并输出结果
    result = ''
    for i in range(len(T)):
        if T[i] == '1':
            result += s1
        elif T[i] == '2':
            result += s2
        else:
            result += s3
    print(result)

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in t:
        if i == "1":
            print(s1, end="")
        elif i == "2":
            print(s2, end="")
        else:
            print(s3, end="")
    print()

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ''
    for i in t:
        if i == '1':
            ans = ans + s1
        elif i == '2':
            ans = ans + s2
        else:
            ans = ans + s3
    print(ans)

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in t:
        if i == "1":
            ans += s1
        elif i == "2":
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in range(len(t)):
        if t[i] == '1':
            print(s1,end='')
        elif t[i] == '2':
            print(s2,end='')
        else:
            print(s3,end='')
    print()

=======
Suggestion 10

def main():
    # 读取输入
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    # 处理并输出
    for i in range(len(t)):
        if t[i] == '1':
            print(s1, end='')
        elif t[i] == '2':
            print(s2, end='')
        elif t[i] == '3':
            print(s3, end='')
