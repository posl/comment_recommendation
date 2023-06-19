Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in range(len(t)):
        if t[i] == "1":
            result += s1
        elif t[i] == "2":
            result += s2
        elif t[i] == "3":
            result += s3
    print(result)

=======
Suggestion 2

def get_s(s, t):
    s1 = ''
    for i in range(len(t)):
        if t[i] == '1':
            s1 += s[0]
        elif t[i] == '2':
            s1 += s[1]
        else:
            s1 += s[2]
    return s1

s1 = input()
s2 = input()
s3 = input()
t = input()
print(get_s(s1, t) + get_s(s2, t) + get_s(s3, t))

=======
Suggestion 3

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
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        else:
            result += s3
    print(result)

=======
Suggestion 5

def main():
    # 读取输入
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    # 计算结果
    result = ""
    for i in t:
        if i == '1':
            result += s1
        elif i == '2':
            result += s2
        else:
            result += s3

    # 打印结果
    print(result)

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in range(len(t)):
        if t[i] == "1":
            ans += s1
        elif t[i] == "2":
            ans += s2
        elif t[i] == "3":
            ans += s3
    print(ans)

=======
Suggestion 7

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
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = []
    for i in range(len(t)):
        if t[i] == '1':
            result.append(s1)
        elif t[i] == '2':
            result.append(s2)
        elif t[i] == '3':
            result.append(s3)
    print(''.join(result))

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ''
    for i in range(len(t)):
        if t[i] == '1':
            ans += s1
        elif t[i] == '2':
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 10

def main():
    # 读入三个字符串
    s1 = input()
    s2 = input()
    s3 = input()
    # 读入T
    T = input()
    # 用T中的字符决定输出的字符
    ans = ""
    for i in T:
        if i == "1":
            ans += s1
        elif i == "2":
            ans += s2
        else:
            ans += s3
    # 打印答案
    print(ans)
