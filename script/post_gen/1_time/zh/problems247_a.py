Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(S[1:]+S[0])

=======
Suggestion 2

def main():
    str = input()
    print(str[1:] + str[0])

=======
Suggestion 3

def main():
    # 输入
    S = input()

    # 处理
    S = S.replace('1', '2').replace('0', '1').replace('2', '0')

    # 输出
    print(S)

=======
Suggestion 4

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 5

def problem247_a():
    s = input()
    result = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            result += "0"
        else:
            result += s[i + 1]
    print(result)

problem247_a()

=======
Suggestion 6

def problems247_a():
    S = str(input())
    s = list(S)
    s.append(s[0])
    s.pop(0)
    print("".join(s))

=======
Suggestion 7

def main():
    s = input()
    s = s.replace("1", "2")
    s = s.replace("0", "1")
    s = s.replace("2", "0")
    print(s)

=======
Suggestion 8

def problem247_a(s):
    # print(s)
    s = s.replace('1','2')
    s = s.replace('0','1')
    s = s.replace('2','0')
    print(s)

problem247_a('1011')
problem247_a('0000')
problem247_a('1111')
