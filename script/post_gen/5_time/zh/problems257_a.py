Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    print(chr(ord('A') + (X - 1) % 26))

=======
Suggestion 2

def get_char(n, x):
    # 从字符串的开头找出第X个字符，这个字符串是由这些字符串联而成的：A的N份，B的N份，...，Z的N份，按这个顺序排列。
    # 1 ≦ N ≦ 100
    # 1 ≦ X ≦ N× 26
    # 输入的所有数值都是整数。
    # 输入是由标准输入提供的，格式如下：
    # N X
    # 打印答案。
    # 输入样本 1
    # 1 3
    # 样本输出 1
    # C
    # 我们得到字符串ABCDEFGHIJKLMNOPQRSTUVWXYZ，其从头开始的第3个字符是C。
    # 输入样本2
    # 2 12
    # 样本输出 2
    # F
    # 我们得到字符串AABBCCDDEEFFGGHHIIJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ，其从头开始的第12个字符是F。
    # print(n, x)
    if n < 1 or n > 100:
        return
    if x < 1 or x > n * 26:
        return
    # 字母表
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print(alp)
    # 重复N次
    alp = alp * n
    # print(alp)
    # 获取第x个字符
    return alp[x - 1]

=======
Suggestion 3

def get_char(n, x):
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return char[(x - 1) % 26]

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    n = n - 1
    x = x - 1
    print(chr(65 + x % 26))

=======
Suggestion 5

def problems257_a():
    n, x = map(int, input().split())
    s = ''
    for i in range(26):
        s += chr(65+i) * n
    print(s[x-1])

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + (x - 1) % 26))

=======
Suggestion 7

def get_char(n, x):
    if x % n == 0:
        return chr(64 + n)
    else:
        return chr(64 + x % n)

=======
Suggestion 8

def getNthChar(n, x):
    if n == 1:
        return chr(ord('A') + x - 1)
    else:
        return chr(ord('A') + x - 1 + (n - 1) * 26)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))

=======
Suggestion 10

def main():
    n,x = map(int, input().split())
    ans = ""
    for i in range(0, n):
        ans += chr(65 + i) * n
    print(ans[x-1])
