Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def plural_form(string):
    if string[-1] == 's':
        return string + 'es'
    else:
        return string + 's'

=======
Suggestion 2

def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 3

def pluralize(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

=======
Suggestion 4

def main():
    s = input()
    if s.endswith("s"):
        print(s + "es")
    else:
        print(s + "s")

=======
Suggestion 5

def main():
    # 读入数据
    s = input()
    # 处理数据
    if s[-1] == 's':
        s += 'es'
    else:

=======
Suggestion 6

def plural(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 7

def plural_form(word):
    if word[-1] == "s":
        return word + "es"
    else:
        return word + "s"

=======
Suggestion 8

def pluralize(s):
    if s.endswith('s') or s.endswith('sh') or s.endswith('ch') or s.endswith('o') or s.e

=======
Suggestion 9

def getPluralForm(input):
    if input[-1] == "s":
        return input + "es"
    else:
        return input + "s"
