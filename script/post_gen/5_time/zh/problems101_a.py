Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    S = input()

    # process
    answer = 0
    for s in S:
        if s == '+':
            answer += 1
        else:
            answer -= 1

    # output
    print(answer)

=======
Suggestion 2

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 3

def main():
    S = input()
    sum = 0
    if S[0] == '+':
        sum += 1
    elif S[0] == '-':
        sum -= 1
    if S[1] == '+':
        sum += 1
    elif S[1] == '-':
        sum -= 1
    if S[2] == '+':
        sum += 1
    elif S[2] == '-':
        sum -= 1
    if S[3] == '+':
        sum += 1
    elif S[3] == '-':
        sum -= 1
    print(sum)

=======
Suggestion 4

def solve():
    s = input()
    res = 0
    for i in range(4):
        if s[i] == '+':
            res += 1
        else:
            res -= 1
    print(res)

=======
Suggestion 5

def main():
    S = input()
    num = 0
    for i in range(4):
        if S[i] == '+':
            num += 1
        else:
            num -= 1
    print(num)

=======
Suggestion 6

def main():
    S = input()
    sum = 0
    for i in range(4):
        if S[i] == "+":
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 7

def main():
    s = raw_input()
    print s.count('+') - s.count('-')

=======
Suggestion 8

def main():
    s = input()
    num = 0
    for i in s:
        if i == '+':
            num += 1
        else:
            num -= 1
    print(num)

=======
Suggestion 9

def main():
    input_str = input()
    sum = 0
    for i in range(4):
        if input_str[i] == "+":
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 10

def main():
    #读入字符串
    s = input()
    #初始化结果
    result = 0
    #循环处理字符串
    for i in range(4):
        #如果是+，则加1
        if s[i] == '+':
            result += 1
        #如果是-，则减1
        else:
            result -= 1
    #打印结果
    print(result)
