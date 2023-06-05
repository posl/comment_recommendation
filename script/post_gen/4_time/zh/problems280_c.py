Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #读取输入
    S = input()
    T = input()
    #判断S与T的长度
    len_S = len(S)
    len_T = len(T)
    #判断S与T的长度是否符合约束
    if 1 <= len_S <= 5*10**5 and 1 <= len_T <= 5*10**5:
        #判断S与T的长度是否相等
        if len_S == len_T - 1:
            #遍历S
            for i in range(len_S):
                #判断S与T的第i个字符是否相同
                if S[i] != T[i]:
                    #输出i+1
                    print(i+1)
                    #跳出循环
                    break
            else:
                #输出len_T
                print(len_T)
        else:
            #输出len_T
            print(len_T)
    else:
        #输出len_T
        print(len_T)

=======
Suggestion 2

def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)

solve()

=======
Suggestion 3

def solve(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i + 1

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(t)):
        if t[:i] + t[i+1:] == s:
            print(i+1)
            break

=======
Suggestion 5

def main():
    s = input()
    t = input()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i = i + 1
        j = j + 1
    print(j)

=======
Suggestion 6

def main():
    s = input()
    t = input()

    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 7

def solve(s,t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i+1
    return len(s)+1

=======
Suggestion 8

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    for i in range(len(t)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(t))

=======
Suggestion 10

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

main()
