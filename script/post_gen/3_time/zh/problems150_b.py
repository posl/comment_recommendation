Synthesizing 10/10 solutions

=======
Suggestion 1

def problems150_b():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 6

def problems150_b():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 8

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 9

def main():
    #输入
    N = int(input())
    S = input()
    #计算ABC出现的次数
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    #输出
    print(count)

=======
Suggestion 10

def countABC(s):
    # s = 'ZABCDBABCQ'
    # s = '3-4-5'
    # s = 'abccabcbabccabacbcbbabcbcbcabcb'
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == 'ABC':
            count += 1
    return count
