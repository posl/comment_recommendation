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
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

=======
Suggestion 3

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

=======
Suggestion 4

def plural_form(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 5

def plural(word):
    if word[-1] == 's':
        return word + 'es'
    return word + 's'

=======
Suggestion 6

def plural_form(s):
    if s.endswith("s"):
        return s + "es"
    else:
        return s + "s"

=======
Suggestion 7

def plural_form():
    string = input()
    if string.endswith('s'):
        print(string + 'es')
    else:
        print(string + 's')

=======
Suggestion 8

def pluralize(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

print(pluralize(input()))

I have a problem with the third test case. It says that the output should be "boxs", but it should be "boxes". Is it a typo or am I wrong?

I can't find any typo in the problem statement. I think it's a typo. Could someone confirm this?

I think it's a typo. I've seen people asking the same question on the forum, and the author of the problem said that it's a typo.
