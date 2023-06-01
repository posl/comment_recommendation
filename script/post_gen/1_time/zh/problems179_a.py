Synthesizing 10/10 solutions (Duplicates hidden)

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
    s = input()
    if s[-1] == "s":
        print(s + "es")
    else:
        print(s + "s")

=======
Suggestion 3

def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 4

def problem179_a():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 5

def plural(s):
    if s[-1] == 's':
        return s+'es'
    else:
        return s+'s'

print(plural(input()))

=======
Suggestion 6

def plural_form(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

=======
Suggestion 7

def main():
    # 读取输入
    s = input()
    # 根据题意，判断单词s是否以s结尾
    if s[-1] == 's':
        # 如果是，则在单数形式的末尾加上es
        print(s + 'es')
    else:
        # 如果不是，则在单数形式的后面加上s
        print(s + 's')
