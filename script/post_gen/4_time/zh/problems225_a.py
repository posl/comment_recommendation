Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    s = input()
    return s

=======
Suggestion 2

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 3

def main():
    # 读入S
    S = input()
    # 通过交换S中的字符可以得到的不同字符串的数量
    print(len(set(S)))

=======
Suggestion 4

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 5

def main():
    S = input()
    if len(S) == 3:
        print(6)
    elif len(S) == 2:
        print(2)
    else:
        print(1)

main()

=======
Suggestion 6

def main():
    s = input()
    count = 0
    for i in range(3):
        if s[i] == "a":
            count += 1
    if count == 1:
        print(1)
    elif count == 2:
        print(3)
    elif count == 3:
        print(6)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    s = input()
    # 初始化变量
    ans = 0
    # 穷举
    for i in range(3):
        for j in range(i+1, 3):
            if s[i] != s[j]:
                ans += 1
    # 打印输出
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    s1 = S[0]
    s2 = S[1]
    s3 = S[2]
    if s1 == s2 == s3:
        print(1)
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print(3)
    else:
        print(6)
