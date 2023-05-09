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
    s = input()
    if s.endswith('s'):
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 3

def main():
    S = input()
    if S[-1] == "s":
        print(S+"es")
    else:
        print(S+"s")

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

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 6

def plural_form(word):
    if word[-1] == "s":
        return word + "es"
    else:
        return word + "s"

=======
Suggestion 7

def plural_form(S):
    if S[-1] == 's':
        return S + 'es'
    else:
        return S + 's'

=======
Suggestion 8

def plural_form(S):
    if S[-1] == "s":
        return S + "es"
    else:
        return S + "s"

=======
Suggestion 9

def plural_form(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

=======
Suggestion 10

def plural_form():
    s = input()
    if s.endswith("s"):
        print(s + "es")
    else:
        print(s + "s")

plural_form()
