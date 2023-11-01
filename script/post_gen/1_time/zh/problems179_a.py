Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def plural_form(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 2

def getPluralForm(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 3

def pluralize(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'

=======
Suggestion 4

def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 5

def main():
    s = input()
    if s.endswith('s'):
        print(s + 'es')
    else:
        print(s + 's')

=======
Suggestion 6

def pluralize(s):
  if s[-1] == "s":
    return s + "es"
  else:
    return s + "s"
