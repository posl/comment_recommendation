Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 2

def main():
    S = input()
    if S[-1] == "s":
        print(S + "es")
    else:
        print(S + "s")

=======
Suggestion 3

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 4

def pluralize(word):
    if word.endswith('s'):
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 5

def pluralize(noun):
    if noun.endswith('s'):
        return noun + 'es'
    else:
        return noun + 's'

=======
Suggestion 6

def plural_form(string):
    if string[-1] == "s":
        return string + "es"
    else:
        return string + "s"

=======
Suggestion 7

def plural_form(s):
    if s.endswith('s'):
        return s + 'es'
    return s + 's'
