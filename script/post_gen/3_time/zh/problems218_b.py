Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = list(map(int, input().split()))
    alpha = [chr(i) for i in range(97, 123)]
    S = [alpha[i-1] for i in P]
    print(''.join(S))

=======
Suggestion 2

def main():
    P = input().split()
    S = [chr(int(P[i])+96) for i in range(26)]
    print(''.join(S))

=======
Suggestion 3

def main():
    P = list(map(int, input().split()))
    S = ''
    for i in range(26):
        S += chr(ord('a') + P[i] - 1)
    print(S)

=======
Suggestion 4

def main():
    a = [int(x) for x in input().split()]
    b = [chr(x+96) for x in a]
    print("".join(b))

main()

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    print(''.join(chr(ord('a') + x - 1) for x in p))

=======
Suggestion 6

def main():
    # 读入数据
    p = list(map(int, input().split()))
    # 生成字母表
    alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    # 生成字典
    d = dict(zip(p, alphabet))
    # 输出
    for i in range(1, 27):
        print(d[i], end='')

=======
Suggestion 7

def main():
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    for i in range(26):
        print(chr(s[i]+96), end = '')

=======
Suggestion 8

def main():
    P = input().split()
    P = list(map(int, P))
    P = [chr(96 + i) for i in P]
    print(''.join(P))

=======
Suggestion 9

def printStr(p):
    str = ""
    for i in range(len(p)):
        str = str + chr(p[i]+96)
    print(str)

p = list(map(int, input().split()))
printStr(p)

=======
Suggestion 10

def main():
    s = input()
    ls = s.split()
    for i in range(26):
        ls[i] = int(ls[i])
    for i in range(26):
        print(chr(ls[i]+96),end='')
    print()
