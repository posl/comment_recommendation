Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    s = input()
    # 判断最后一个字符是否为s
    if s[-1] == 's':
        print(s + 'es')
    else:

=======
Suggestion 2

def plural_form(S):
    if S[-1] == "s":
        return S + "es"
    else:
        return S + "s"

=======
Suggestion 3

def plural_form(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 4

def main():
    s = input()
    if s[len(s)-1] == "s":
        print(s + "es")
    else:
        print(s + "s")

=======
Suggestion 5

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 6

def plural_form(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 7

def main():
    S = input()
    if S.endswith('s'):
        print(S+'es')
    else:
        print(S+'s')

=======
Suggestion 8

def main():
    # 读取输入
    s = input()
    # 处理
    if s.endswith('s') or s.endswith('x') or s.endswith('o') or

=======
Suggestion 9

def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 10

def plural_form_of_noun(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'
