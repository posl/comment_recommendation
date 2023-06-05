Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 2

def problem126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1]+s[k-1].lower()+s[k:])

=======
Suggestion 3

def replace_str_char(str_text, index=0, char=''):
    str_list = list(str_text)
    str_list[index] = char
    return ''.join(str_list)

=======
Suggestion 4

def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 解决方案
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 5

def main():
    # 1. 获取输入
    n, k = map(int, input().split())
    s = input()
    # 2. 处理
    result = s[:k-1] + s[k-1].lower() + s[k:]
    # 3. 输出
    print(result)

=======
Suggestion 6

def problem126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1]+s[k-1].lower()+s[k:])

problem126_a()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    S = S[:K-1] + S[K-1].lower() + S[K:]
    print(S)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1]+s[k-1].lower()+s[k:])

=======
Suggestion 9

def problems126_a():
    N,K = map(int,input().split())
    S = input()
    print(S[:K-1]+S[K-1].lower()+S[K:])
