Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[-1] == "s":
        print(S + "es")
    else:
        print(S + "s")

=======
Suggestion 2

def plural(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 3

def pluralize(noun):
    if noun.endswith('s'):
        return noun + 'es'
    else:
        return noun + 's'

print(pluralize('apple'))
print(pluralize('bus'))
print(pluralize('box'))

=======
Suggestion 4

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 5

def plural_form(s):
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

s = input()
plural_form(s)

=======
Suggestion 6

def pluralForm(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

print(pluralForm(input()))

=======
Suggestion 7

def pluralize(word):
    if word[len(word)-1] == 's':
        word += 'es'
    else:
        word += 's'
    return word

=======
Suggestion 8

def plural_form(S):
    if S.endswith('s'):
        return S + 'es'
    else:
        return S + 's'

=======
Suggestion 9

def pluralize_word(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 10

def plural_form(s):
    if s.endswith('s'):
        print(s + 'es')
    else:
        print(s + 's')
