Synthesizing 10/10 solutions

=======
Suggestion 1

def count_ABCs(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 2

def main():
    # 读取输入
    n = int(input())
    s = input()
    # 计数
    count = 0
    # 遍历
    for i in range(n - 2):
        # 判断
        if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            count += 1
    # 输出
    print(count)

=======
Suggestion 3

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 4

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 8

def count_abc(s):
    count = 0
    for i in range(0, len(s)):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 9

def get_str():
    num = int(input())
    str = input()
    return num,str

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)
