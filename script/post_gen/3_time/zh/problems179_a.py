Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[-1] == 's':
        print(S+'es')
    else:
        print(S+'s')

=======
Suggestion 2

def main():
    # 读入
    S = input()
    # 处理
    if S[-1] == 's':
        S += 'es'
    else:
        S += 's'
    # 输出
    print(S)

=======
Suggestion 3

def plural(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

=======
Suggestion 4

def main():
    S = input()
    if S.endswith('s'):
        print(S + 'es')
    else:
        print(S + 's')

=======
Suggestion 5

def main():
    s = input()
    if s[-1] == "s":
        print(s + "es")
    else:
        print(s + "s")

=======
Suggestion 6

def solve():
    S = input()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

=======
Suggestion 7

def pluralize(S):
    if S[-1] == 's':
        return S + 'es'
    else:
        return S + 's'
