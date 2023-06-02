Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

=======
Suggestion 2

def main():
    # 读取数据
    S = input()
    # 计算结果
    if S[-1] == "s":
        print(S + "es")
    else:
        print(S + "s")

=======
Suggestion 3

def plural_form(S):
    if S[-1] == 's':
        return S + 'es'
    else:
        return S + 's'

=======
Suggestion 4

def main():
    S = input()
    if S[-1] == "s":
        S = S + "es"
    else:
        S = S + "s"
    print(S)

=======
Suggestion 5

def pluralize(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

s = input()
print(pluralize(s))

=======
Suggestion 6

def plural(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

print(plural(input()))

=======
Suggestion 7

def pluralForm(S):
    if S[-1] == "s":
        return S + "es"
    else:
        return S + "s"

=======
Suggestion 8

def solve():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 9

def plural_form(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 10

def pluralize(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'
