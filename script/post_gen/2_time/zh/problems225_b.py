Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 请在此添加代码，实现问题解决方案
    s = input()
    # print(s)
    # print(len(s))
    # print(s[0])
    # print(s[1])
    # print(s[2])
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print(3)
        else:
            print(6)
    else:
        print("字符串长度不为3")

=======
Suggestion 2

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 3

def f(s):
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    if len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            return 1
        elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
            return 3
        else:
            return 6

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    S.sort()
    count = 1
    for i in range(2):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    print(len(set(S)))
main()

=======
Suggestion 6

def swap(s, i, j):
    t = s[i]
    s[i] = s[j]
    s[j] = t
