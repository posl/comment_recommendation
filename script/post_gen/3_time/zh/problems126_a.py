Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

N, K = map(int, input().split())
S = input()
print(change_char(S, K-1, S[K-1].lower()))

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

main()

=======
Suggestion 4

def main():
    # 读取输入
    N, K = map(int, input().split())
    S = input()
    # 通过列表解析替换第K个字符
    S_new = S[:K-1] + S[K-1].lower() + S[K:]
    print(S_new)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])

=======
Suggestion 6

def problems126_a():
	n,k = map(int,input().split())
	s = input()
	s = s[:k-1] + s[k-1].lower() + s[k:]
	print(s)

=======
Suggestion 7

def underline(s, k):
    return s[:k-1] + s[k-1].lower() + s[k:]

=======
Suggestion 8

def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 按照题目要求输出
    print(s[:k-1] + s[k-1].lower() + s[k:])
