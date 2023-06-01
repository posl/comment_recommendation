Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    r = s.count('0')
    b = len(s) - r
    print(min(r, b) * 2)

=======
Suggestion 2

def main():
    # 读入数据
    str = input()
    # 计算数据
    count0 = 0
    count1 = 0
    for i in range(len(str)):
        if str[i] == '0':
            count0 += 1
        else:
            count1 += 1
    # 输出结果
    print(min(count0, count1) * 2)

=======
Suggestion 3

def main():
    S = input()
    #print(S)
    #print(type(S))
    #print(len(S))
    #print(S[0])

    #从左到右依次遍历，如果是0则入栈，如果是1则出栈，如果出栈的时候栈为空则将结果+1
    stack = []
    result = 0
    for i in range(len(S)):
        if S[i] == '0':
            stack.append(S[i])
        else:
            if len(stack) == 0:
                result += 1
            else:
                stack.pop()

    #从右到左依次遍历，如果是1则入栈，如果是0则出栈，如果出栈的时候栈为空则将结果+1
    stack = []
    for i in range(len(S)-1, -1, -1):
        if S[i] == '1':
            stack.append(S[i])
        else:
            if len(stack) == 0:
                result += 1
            else:
                stack.pop()

    print(result)

=======
Suggestion 4

def main():
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(0,len(s)-1):
        if s[i] == '0':
            count += 1
        elif s[i] == '1' and s[i+1] == '0':
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if S[i] == '1':
            count += 1
    print(min(count, N - count) * 2)

=======
Suggestion 6

def main():
    S = input()
    #print(S)
    #print(len(S))
    #print(type(S))
    #print(S[0])
    #print(type(S[0]))
    #print(S[0] == '0')
    #print(S[0] == '1')
    #print(S[0] == 0)
    #print(S[0] == 1)
    #print(S[0] == 2)
    #print(S[0] == 3)
    #print(S[0] == 4)
    #print(S[0] == 5)
    #print(S[0] == 6)
    #print(S[0] == 7)
    #print(S[0] == 8)
    #print(S[0] == 9)
    #print(S[0] == 10)
    #print(S[0] == 11)
    #print(S[0] == 12)
    #print(S[0] == 13)
    #print(S[0] == 14)
    #print(S[0] == 15)
    #print(S[0] == 16)
    #print(S[0] == 17)
    #print(S[0] == 18)
    #print(S[0] == 19)
    #print(S[0] == 20)
    #print(S[0] == 21)
    #print(S[0] == 22)
    #print(S[0] == 23)
    #print(S[0] == 24)
    #print(S[0] == 25)
    #print(S[0] == 26)
    #print(S[0] == 27)
    #print(S[0] == 28)
    #print(S[0] == 29)
    #print(S[0] == 30)
    #print(S[0] == 31)
    #print(S[0] == 32)
    #print(S[0] == 33)
    #print(S[0] == 34)
    #print(S[0] == 35)
    #print(S[0] == 36)
    #print(S[0] == 37)
    #print(S[0] == 38)
    #print(S[0] == 39

=======
Suggestion 7

def main():
    s = input()
    r = s.count("0")
    b = s.count("1")
    print(min(r, b) * 2)

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        if s[i] == "1":
            cnt += 1
    print(min(cnt, n - cnt) * 2)

=======
Suggestion 9

def solve():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "1":
            ans += 1
    ans = min(ans, N-ans)
    print(ans)
solve()

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    num = 0
    for i in range(N):
        if S[i] == '1':
            num += 1
    print(min(num, N-num)*2)
